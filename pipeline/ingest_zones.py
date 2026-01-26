import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

def run():

    source_file = 'taxi_zone_lookup.csv'
    table_name = 'taxi_zones'

    df = pd.read_csv(
        source_file,
        nrows = 100
    )

    engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
    print(pd.io.sql.get_schema(df, name=table_name, con=engine))
    
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df_iter = pd.read_csv(
        source_file,
        iterator=True,
        chunksize=100000
    )

    first = True

    for df_chunk in tqdm(df_iter):

        if first:
            # Create table schema (no data)
            df_chunk.head(0).to_sql(
                name=table_name,
                con=engine,
                if_exists="replace"
            )
            first = False
            print(f"Table {table_name} created")

        # Insert chunk
        df_chunk.to_sql(
            name=table_name, 
            con=engine, 
            if_exists="append"
        )

        print("Inserted:", len(df_chunk))


if __name__ == '__main__':
    run()