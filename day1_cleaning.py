import pandas as pd

data = {
    "Name": ["Anas", "Rahim", "John", "Anas", None],
    "Department": [" Sales ", "sales", "HR", " Sales ", "IT"],
    "Salary": [50000, 55000, None, 50000, 60000],
    "Joining_Date": ["01-02-2024", "2024/03/15", "15-04-2024", "01-02-2024", None]
}

df = pd.DataFrame(data)

print(df)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df["Department"]=df["Department"].str.strip().str.title()
print(df)
print(df["Salary"].median())
df["Salary"]=df["Salary"].fillna(df["Salary"].median())
df["Name"]=df["Name"].fillna("Unknown")
print(df)
df=df.drop_duplicates()
print(df)
df["Joining_Date"]=pd.to_datetime(df["Joining_Date"],
dayfirst=True, errors="coerce")
print(df)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
df.loc[1,"Joining_Date"]=pd.to_datetime("2024-03-15")
df["Department"]=df["Department"].str.upper()
print(df)
df.to_csv("cleaned_dataset.csv",index=False)
print("Cleaned dataset saved successfully")