import os
import pandas as pd
from sqlalchemy import create_engine

# Define the path to the database file
db_path = 'AstroCaps.db'

# Ensure the directory exists
if not os.path.exists('db'):
    os.makedirs('db')

# Create an engine that connects to the SQLite database
engine = create_engine(f'sqlite:///instance/{db_path}')

# Load data from CSV file
data = pd.read_csv('data/catalogue-de-messier.csv')

# Convert data types if necessary (e.g., trimming spaces, converting formats)
# For example, if there are spaces in the column names, you might want to trim them
data.columns = data.columns.str.strip()

# Import data into the database
data.to_sql('MessierObjects', con=engine, index=False, if_exists='replace')

print("Data imported successfully.")
