"""precietacxtion starts at 1781"""
#this data comes from https://www.ecad.eu/
import zipfile
import pandas as pd
import os
import glob
pd.set_option("display.width",3000)
pd.set_option("display.max_columns",None)
#from rich import print
#zip_file_path=r"C:\Users\AndrewHayes\OneDrive - Fourteen IP Communications\Desktop\coper\1780-all daily recordds - Copy\adaptor.glamod.retrieve-1713941564.3165028-26302-13-02e41df4-130d-4c07-a74c-b89558bfb339.zip"
extract_dir =r"C:\Users\AndrewHayes\OneDrive - Fourteen IP Communications\Desktop\coper\extracted files"
all_files = []

# with zipfile.ZipFile(zip_file_path,"r") as zip_ref:
#     zip_ref.extractall(extract_dir)

files= glob.glob(extract_dir+ "/*.csv")# thius will select all files with extract folder that are csv, removes need for a for loop

"""def extract_csv_files(zip_file_path, extract_dir):    this only extracts csv files
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        for file_info in zip_ref.infolist():
            if file_info.filename.endswith('.csv'):
                zip_ref.extract(file_info, extract_dir)"""

#columns to keep
keep = ["date_time", "longitude", "latitude","observed_variable",
 "observation_value", "value_significance", "primary_station_id", "station_name", "quality_flag"]



#joins all csv files within folder in one dataframe
for file in files:
    file_path=os.path.join(extract_dir,file)
    all_files.append(pd.read_csv(file_path))
df=pd.concat(all_files,ignore_index=True)
print(df.columns)

#keeps only column wihin keep variale
df_filtered = df.loc[:, keep]



dff=df_filtered.sort_values("station_name")


#changing the long datetime to short date
dff["date_time"] =pd.to_datetime((dff["date_time"]))
dff["year_month"]=dff["date_time"].dt.strftime("%Y-%m")

#drops date_time
dff=dff.drop("date_time",axis=1)


#counts of many of each type of record
value_significance_counts = dff["value_significance"].value_counts()
print(value_significance_counts)



# gives onlfirst 7 charchters in "value_significance" column
dff["value_significance"]=dff["value_significance"].apply(lambda x:x[:7])



print(dff.tail(10))






"""" TASKS
make script to download 12 months atr a time, IF have whole year then make record that is complete
run conversion of K to C before saving a csv or dataframe
combined all 12 months into the 1 filtered dataframe then nsave csv in a cpmpleted folder with thhe year name
each time the program runs it checks last completed year then adds +1 to the year to DL
RERUN download




need to keep record of which years are downloaded"""








# print(x)
# monthly_mean=271.3616667
#
# def tempconversion(x):   #round this off 2 dec
#     calc=x-273.15
#     print(round(calc,2))
#     return round(calc, 2)

#
# tempconversion(x)
# -1.7870967741935146
# -1.7870967741935146






