import os
print(os.getcwd())
import cdsapi
UID=[]
key=[]

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
