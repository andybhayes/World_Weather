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

def extract_csv_files(zip_file_path, extract_dir):
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        for file_info in zip_ref.infolist():
            if file_info.filename.endswith('.csv'):
                zip_ref.extract(file_info, extract_dir)



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






