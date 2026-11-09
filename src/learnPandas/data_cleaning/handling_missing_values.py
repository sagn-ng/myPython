import pandas as pd
import numpy as np

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "melb_data.csv"

melb_house_data = pd.read_csv(csv_path)

"""First look"""
print(melb_house_data.head())
print()

"""Count the number of missing values in each column"""
# get the number of missing data points per column
missing_values_count=melb_house_data.isnull().sum() #isnull(), or isna()
# look at the # of missing points in the first 15 columns
# print(missing_values_count[0:15])

# how many total missing values do we have?
total_cells = np.prod(melb_house_data.shape)
total_missing = missing_values_count.sum()


"""Drop missing values"""
eg_0=melb_house_data.dropna() #remove every row with at least 1 missing value
# print(eg_0)

print()
eg_1=melb_house_data.dropna(axis=1)
# print(eg_1.head())

print()
"""Fill in missing values automatically"""
subset_melb_data=melb_house_data.loc[:, 'Rooms':'YearBuilt'] #extract a small part of the dataset
# print(subset_melb_data.head())

eg_2=subset_melb_data.fillna(0) # replace all NaN's with 0
# print(eg_2)

# replace all NA's the value that comes directly after it in the same column, 
# then replace all the remaining na's with 0
eg_3=subset_melb_data.bfill(axis=0).fillna(0)
print(eg_3)