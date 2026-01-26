import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from tqdm.auto import tqdm

def run():
    source_file = 'green_tripdata_2025-11.parquet'
    table_name = 'green_taxi_202511'
    db_url = 'postgresql://root:root@localhost:5432/ny_taxi'
    
    engine = create_engine(db_url)

    # 1. Use PyArrow to open the Parquet file (doesn't load into RAM yet)
    parquet_file = pq.ParquetFile(source_file)
    
    # 2. Preview the first 100 rows to create the schema
    # We use slice(0, 100) to be efficient
    preview_df = parquet_file.read().slice(0, 100).to_pandas()
    
    print("Schema preview:")
    print(pd.io.sql.get_schema(preview_df, name=table_name, con=engine))

    # 3. Create the table structure (dropping if exists)
    preview_df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')
    print(f"Table {table_name} created.")

    # 4. Iterate through the file in batches (iter_batches)
    # Parquet files are stored in "row groups". iter_batches allows us 
    # to process them without loading the whole file.
    batch_size = 100000
    
    # Total rows for the progress bar
    total_rows = parquet_file.metadata.num_rows
    pbar = tqdm(total=total_rows, desc="Uploading to Postgres")

    for batch in parquet_file.iter_batches(batch_size=batch_size):
        # Convert the PyArrow batch to a Pandas DataFrame
        df_chunk = batch.to_pandas()
        
        # Insert chunk into Postgres
        df_chunk.to_sql(
            name=table_name, 
            con=engine, 
            if_exists="append",
            index=False # Recommended unless you need the index as a column
        )
        
        pbar.update(len(df_chunk))

    pbar.close()
    print("Upload complete!")

if __name__ == '__main__':
    run()