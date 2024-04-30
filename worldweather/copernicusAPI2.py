#gmail accountv - https://cds.climate.copernicus.eu/cdsapp#!/dataset/insitu-observations-surface-land?tab=form
#C:\Users\AndrewHayes\OneDrive - Fourteen IP Communications\Desktop\stuff\Lib\site-packages\cdsapi\api.py"
import os
print(os.getcwd())
t= r"C:\Users\AndrewHayes\OneDrive - Fourteen IP Communications\Desktop\coper\filesviaAPI"
import cdsapi
UID=299291
key="f9b44ab5-e10e-4edf-be42-d1ec97fcdae8"


year=""

def runyear(year):
    c = cdsapi.Client()
    c.retrieve(
        'insitu-observations-surface-land',
        {
            'time_aggregation': 'monthly',
            'variable': 'air_temperature',
            'usage_restrictions': 'restricted',
            'data_quality': 'passed',
            'year': str(year),
            'month': ['01',"02","03","04","05","06","07","08","09","10","11","12"],
            'day': '01',
            'format': 'zip',
        },
        'download.zip')



def yearsdone():
    with open("doneyears.text","a") as file:
        if "year" in file:
            year=int("year")+1
            runyear(year)
        else:
            file.write(year=int("1763"),
            )
            runyear(year)

yearsdone()














"""chat cptr version

def retrieve_data(year):
    c = cdsapi.Client()
    c.retrieve(
        'insitu-observations-surface-land',
        {
            'time_aggregation': 'monthly',
            'variable': 'air_temperature',
            'usage_restrictions': 'restricted',
            'data_quality': 'passed',
            'year': str(year),  # Convert year to string
            'month': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
            'day': '01',
            'format': 'zip',
        },
        f'{year}_download.zip')  # Save with year in the filename


# Function to get the last successfully downloaded year
def get_last_year():
    try:
        with open("last_year.txt", "r") as f:
            last_year = int(f.read())
    except FileNotFoundError:
        last_year = 1763  # Default starting year
    return last_year


# Function to update the last successfully downloaded year
def update_last_year(year):
    with open("last_year.txt", "w") as f:
        f.write(str(year))


def main():
    last_year = get_last_year()
    current_year = 2024

    # Loop from the last successfully downloaded year to the current year
    for year in range(last_year, current_year + 1):
        retrieve_data(year)
        update_last_year(year + 1)  # Update the last year to the next one after successful download


if __name__ == "__main__":
    main()
    
    
In this modified script:

The retrieve_data function now accepts a year as an argument and retrieves data for that year using the cdsapi client.
The get_last_year function retrieves the last successfully downloaded year from the file "last_year.txt" (or a default starting year if the file doesn't exist).
The update_last_year function updates the last successfully downloaded year in the "last_year.txt" file.
In the main function, the script loops from the last successfully downloaded year to the current year, 
downloading data for each year and updating the last successfully downloaded year to the next one after each successful download.    
    
    
    
"""
