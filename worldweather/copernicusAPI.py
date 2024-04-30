#gmail accountv - https://cds.climate.copernicus.eu/cdsapp#!/dataset/insitu-observations-surface-land?tab=form
#C:\Users\AndrewHayes\OneDrive - Fourteen IP Communications\Desktop\stuff\Lib\site-packages\cdsapi\api.py"
import os
print(os.getcwd())
t= r"C:\Users\AndrewHayes\OneDrive - Fourteen IP Communications\Desktop\coper\filesviaAPI"
import cdsapi
UID=299291
key="f9b44ab5-e10e-4edf-be42-d1ec97fcdae8"



year=1763

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