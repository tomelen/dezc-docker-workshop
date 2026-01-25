import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    nrows=100,
    dtype=dtype,
    parse_dates=parse_dates
)

# Display first rows
df.head()

# Display last rows
df.tail()

# Check data types
df.dtypes

# Check data shape
df.shape


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))

df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

df_iter = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000
)

first = True

for df_chunk in tqdm(df_iter, total=14):

    if first:
        # Create table schema (no data)
        df_chunk.head(0).to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="replace"
        )
        first = False
        print("Table created")

    # Insert chunk
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )

    print("Inserted:", len(df_chunk))