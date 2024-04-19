import pandas as pd
from datetime import datetime

# file paths of CSV files
saturday_file = './csvs/data_2023-02-11.csv'
sunday_file = './csvs/data_2023-02-12.csv'

# reading the CSV files into DataFrames
saturday_data = pd.read_csv(saturday_file, sep=';')
sunday_data = pd.read_csv(sunday_file, sep=';')

# combining the DataFrames into one
combined_data = pd.concat([saturday_data, sunday_data])

# adding a column with the file generation date, which is the current date
combined_data['file_generation_date'] = datetime.now().strftime('%Y-%m-%d')

# saving the combined data to a new CSV file
combined_data.to_csv('combined_data.csv', sep=';', index=False)
