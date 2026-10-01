# Elevate-Labs-task1
# Task 1: Data Cleaning and Preprocessing

## Objective

The objective of this task is to clean and preprocess a raw dataset by identifying and handling common data problems such as missing values, duplicate records, inconsistent text formats, date formats, and incorrect data types.

## Tools Used

- Python
- Pandas
- Pydroid 3

## Dataset

A sample customer dataset was created containing the following columns:

- Name
- Age
- Gender
- Country
- Date

The dataset contains missing values, duplicate records, inconsistent text formats, and different data types to demonstrate the data cleaning process.

## Data Cleaning Steps

### 1. Identify Missing Values

Missing values were identified using:

```python
df.isnull().sum()