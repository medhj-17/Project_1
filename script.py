import requests
import pandas as pd
from sqlalchemy import create_engine
from io import StringIO

# API URL AND PARAMS
url_ods126 = "https://opendata.elia.be/api/explore/v2.1/catalog/datasets/ods126/exports/csv"
url_ods134 = "https://opendata.elia.be/api/explore/v2.1/catalog/datasets/ods134/exports/csv"
params= {"delimiter": "|"}

# Sending GET request
response_ods126 = requests.get(url_ods126,params=params)
response_ods134 = requests.get(url_ods134,params=params)

# Check if the request was successful
if response_ods126.status_code == 200:
    df_ods126 = pd.read_csv(StringIO(response_ods126.text),sep="|") # OR read_json
else:
    print(f"Error {response_ods126.status_code}: {response_ods126.text}")

if response_ods134.status_code == 200:
    df_ods134 = pd.read_csv(StringIO(response_ods134.text),sep="|")
else:
    print(f"Error {response_ods134.status_code}: {response_ods134.text}")

# Filter for September 2024
df_ods126['datetime'] = pd.to_datetime(df_ods126['datetime'])
df_ods126_september_2024 = df_ods126[(df_ods126['datetime'].dt.year == 2024) & (df_ods126['datetime'].dt.month == 9)]

df_ods134['datetime'] = pd.to_datetime(df_ods134['datetime'])
df_ods134_september_2024 = df_ods134[(df_ods134['datetime'].dt.year == 2024) & (df_ods134['datetime'].dt.month == 9)]

# Database configuration
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "testpass"
DB_HOST = "localhost"
DB_PORT = "5432"

# Create a connection to PostgreSQL
db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

# Store data in PostgreSQL
df_ods126_september_2024.to_sql("ods126_september_2024", engine, if_exists="replace", index=False)
df_ods134_september_2024.to_sql("ods134_september_2024", engine, if_exists="replace", index=False)

print("Data successfully stored in PostgreSQL.")