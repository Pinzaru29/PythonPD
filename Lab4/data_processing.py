# Import necessary libraries
import os
import pandas as pd

# Get the directory where the current script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Set the working directory to the script's directory
os.chdir(script_directory)

spotify_data = pd.read_csv('spotify-2023.csv') # Read from CSV file

X_data = spotify_data.drop(columns=['released_year','released_month','released_day']) # Delete some of columns and assign to X_data variable
Y_data = spotify_data[['released_year','released_month','released_day']]              # Assign 3 columns to Y_data variable

# Create new column and save a string of date
spotify_data['date_string'] = spotify_data['released_year'].astype(str) + '-' + spotify_data['released_month'].astype(str) + '-' + spotify_data['released_day'].astype(str)

# Convert date_string column to date_time type variable and assign to new release_date column
spotify_data['release_date'] = pd.to_datetime(spotify_data['date_string'], format='%Y-%m-%d')

# Delete temporary column
spotify_data.drop(columns=['date_string'], inplace=True)

spotify_datetime = spotify_data.drop(columns=['released_year', 'released_month', 'released_day'])

# Define weeks based on the release_date column
spotify_datetime['week'] = spotify_datetime['release_date'].dt.strftime('%Y-%U')

def get_dataFiles_ymd(target_date):
    Y_data = pd.read_csv('Y.csv')

    Y_data['release_date'] = pd.to_datetime(Y_data['released_year'].astype(str) + '-' + Y_data['released_month'].astype(str) + '-' + Y_data['released_day'].astype(str), format='%Y-%m-%d')
    matching_rows = Y_data[Y_data['release_date'] == target_date] # Fined matching rows where date == target_date

    if not matching_rows.empty:
        # Save all matching data
        matching_data = X_data.iloc[matching_rows.index]
        if not matching_data.empty:
            print(matching_data)
            return matching_data
        else:
            print(None)
        return None
    else:
        print(None)
        return None


def get_data_yw(target_date):
    filtered_data_by_week = spotify_datetime[spotify_datetime['week'] == target_date]

    if not filtered_data_by_week.empty:
        print(filtered_data_by_week)
        return filtered_data_by_week
    else:
        print(None)
        return None

def get_data_ymd(target_date):
    filtered_data_by_ymd = spotify_datetime[spotify_datetime['release_date'] == target_date]

    if not filtered_data_by_ymd.empty:
        print(filtered_data_by_ymd)
        return filtered_data_by_ymd
    else:
        print(None)
        return None
