import os
import pandas as pd
import cdsapi
import glob
print(os.getcwd())
pd.set_option("display.width",3000)
pd.set_option("display.max_columns",None)


all_files = []
extract_dir =r""
files= glob.glob(extract_dir+ "/*.csv")# thius will select all files with extract folder that are csv, removes need for a for loop


keep = ["date_time", "longitude", "latitude","observed_variable",
 "observation_value", "value_significance", "primary_station_id", "station_name", "quality_flag"]



#joins all csv files within folder in one dataframe
for file in files:
    file_path=os.path.join(extract_dir,file)
    all_files.append(pd.read_csv(file_path))
df=pd.concat(all_files,ignore_index=True)


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



# gives onlfirst 7 charchters in "value_significance" column
dff["value_significance"]=dff["value_significance"].apply(lambda x:x[:7])

file_date=dff
print(dff.tail(10))
print(dff.shape)
dff.to_csv()
