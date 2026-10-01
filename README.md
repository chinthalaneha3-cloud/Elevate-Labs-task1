# Data Cleaning and Preprocessing

## Objective
To clean and preprocess a raw dataset by handling missing values, duplicate records, inconsistent text, date formats, and incorrect data types.

## Tools Used
- Python
- Pandas
- Pydroid 3

## Dataset
The dataset contains customer information with the following columns:
- Name
- Age
- Gender
- Country
- Date

## Data Cleaning Process

The following steps were performed:

1. Checked for missing values using `isnull()`.
2. Filled missing values with suitable values.
3. Removed duplicate rows using `drop_duplicates()`.
4. Standardized Gender values such as `Male`, `male`, and `FEMALE`.
5. Standardized country names.
6. Converted the Date column into datetime format.
7. Cleaned column names by converting them to lowercase.
8. Corrected data types such as Age to integer.

## Result

After cleaning:

- No missing values remain.
- Duplicate records were removed.
- Text values are standardized.
- Dates are in a consistent format.
- Column names are clean and uniform.
- Data types are corrected.

## Output

The cleaned dataset is ready for further data analysis and visualization.

**Status:** Completed Successfully ✅