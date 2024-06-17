import os
print(os.getcwd())
import cdsapi
UID=[]
key=[]

year=""


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
    
    

