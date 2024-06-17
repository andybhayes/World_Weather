
#This data comes from https://www.ecad.eu/
import zipfile
import pandas as pd
import os
import glob
os.chdir(r"")
pd.set_option("display.width",3000)
pd.set_option("display.max_columns",None)
extract_dir =""
zip_dir =""
zip_files = []
all_files=[]


for root, dirs, files in os.walk(zip_dir):
    for file_name in files:
        if file_name.endswith('.zip'):
            zip_files.append(os.path.join(root, file_name))

# Extract all found zip files
for zip_file_path in zip_files:
    try:
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(extract_dir)
            print(f"Extracted: {zip_file_path}")
    except PermissionError as e:
        print(f"Permission denied: {zip_file_path}. Error: {e}")
    except zipfile.BadZipFile as e:
        print(f"Bad zip file: {zip_file_path}. Error: {e}")
with zipfile.ZipFile(zip_file_path,"r") as zip_ref:
    zip_ref.extractall(extract_dir)

files= glob.glob(extract_dir+ "/*.csv")# thius will select all files with extract folder that are csv, removes need for a for loop



#columns to keep
keep = ["date_time", "longitude", "latitude",
 "observation_value", "value_significance", "primary_station_id", "station_name", "quality_flag"]
#
#
#
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

# gives onlfirst 7 charchters in "value_significance" column
dff["value_significance"]=dff["value_significance"].apply(lambda x:x[:7])

#Convert K to degrees C
dff["observation_value"] = (dff["observation_value"] - 273.15).round(2)

dff=dff.sort_values("year_month", ascending=False)
dff.to_parquet("weatherparquet")
#Save the filtered DataFrame to CSV files based on the year_month range
dff[dff["year_month"] < "1800-01"].to_csv("1700-1800.csv", index=False)
dff[(dff["year_month"] >= "1800-01") & (dff["year_month"] < "1900-01")].to_csv("1800-1900.csv", index=False)
dff[(dff["year_month"] >= "1900-01") & (dff["year_month"] < "1950-01")].to_csv("1900-1950.csv", index=False)
dff[(dff["year_month"] >= "1950-01") & (dff["year_month"] < "1960-01")].to_csv("1950-1959.csv", index=False)
dff[(dff["year_month"] >= "1960-01") & (dff["year_month"] < "1970-01")].to_csv("1960-1969.csv", index=False)
dff[(dff["year_month"] >= "1970-01") & (dff["year_month"] < "1980-01")].to_csv("1970-1979.csv", index=False)
dff[(dff["year_month"] >= "1980-01") & (dff["year_month"] < "1990-01")].to_csv("1980-1989.csv", index=False)
dff[(dff["year_month"] >= "1990-01") & (dff["year_month"] < "2000-01")].to_csv("1990-1999.csv", index=False)
dff[dff["year_month"] >= "2000-01"].to_csv("2000_plus.csv", index=False)

