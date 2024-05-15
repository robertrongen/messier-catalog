import pandas as pd
from sqlalchemy import create_engine

# Create an engine that connects to the SQLite database
engine = create_engine('sqlite:///AstroCaps.db')

# Load data from CSV file
data = pd.read_csv('catalogue-de-messier.csv')

# Convert data types if necessary (e.g., trimming spaces, converting formats)

# Import data into the database
data.to_sql('messier_objects', con=engine, index=False, if_exists='replace')
