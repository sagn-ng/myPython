import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data) #load data into a DataFrame object:
print(type(df))
print(df)

print("\nAccess a row")
print(df.loc[0]) #refer to the row index (this e.g returns the first (0_th) row)

print("\nAccess multiple rows")
print(df.loc[[0, 1]]) #return row 0 and 1

print("\nCreate our own labels (indexes)")
eg = pd.DataFrame(data, index = ["day1", "day2", "day3"]) #self-created labels
print(eg)

print("\nAccess a row with named label")
print(eg.loc["day2"]) #refer to the named index

print("\nAccess a column")
calories_Col=df["calories"]
print(type(calories_Col)) #Series
print(calories_Col)

print("\nAccess multiple rows and columns")
eg=df.loc[0:2, ['calories']] #return the first 2 rows and the 'calories' column
print(eg)

print("\nAccess rows based on conditions")
eg=df[df['duration']>40] #filter rows that have 'duration' > 40
print(eg)

print("\nAccess a specific cell")
C=df.at[0, 'duration'] #access the 'duration' attribute of row 2
print(C)