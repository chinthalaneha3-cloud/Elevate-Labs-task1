import pandas as pd

# --------------------------------
# 1. Create Raw Dataset
# --------------------------------

data = {
    "Name": ["John", "Mary", "John", "David", None, "Sarah"],
    "Age": [25, 30, 25, None, 28, 35],
    "Gender": ["Male", "Female", "Male", "male", "Female", "FEMALE"],
    "Country": ["India", "USA", "India", "India", "USA", "india"],
    "Date": ["01-01-2025", "02-01-2025", "01-01-2025",
             "03-01-2025", None, "04-01-2025"]
}

df = pd.DataFrame(data)

print("===== ORIGINAL DATASET =====")
print(df)

# --------------------------------
# 2. Check Missing Values
# --------------------------------

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# --------------------------------
# 3. Handle Missing Values
# --------------------------------

# Fill missing Name
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Gender
df["Gender"] = df["Gender"].fillna("Unknown")

# Fill missing Country
df["Country"] = df["Country"].fillna("Unknown")

# Fill missing Date
df["Date"] = df["Date"].fillna("01-01-2025")

# --------------------------------
# 4. Remove Duplicate Rows
# --------------------------------

df = df.drop_duplicates()

# --------------------------------
# 5. Standardize Text Values
# --------------------------------

df["Gender"] = df["Gender"].str.lower()

df["Gender"] = df["Gender"].replace({
    "male": "Male",
    "female": "Female"
})

df["Country"] = df["Country"].str.title()

# --------------------------------
# 6. Convert Date Format
# --------------------------------

df["Date"] = pd.to_datetime(
    df["Date"],
    format="%d-%m-%Y"
)

# --------------------------------
# 7. Fix Data Types
# --------------------------------

df["Age"] = df["Age"].astype(int)

# --------------------------------
# 8. Clean Column Names
# --------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# --------------------------------
# 9. Display Cleaned Dataset
# --------------------------------

print("\n===== CLEANED DATASET =====")
print(df)

# --------------------------------
# 10. Check Final Data
# --------------------------------

print("\n===== FINAL MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\nData Cleaning and Preprocessing Completed Successfully!")