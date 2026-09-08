Day 1 – Data Cleaning and Preprocessing

Project Overview

This project focuses on cleaning and preprocessing a raw dataset using Python and Pandas.

The dataset contains common data quality issues such as missing values, duplicate records, inconsistent text formatting, and mixed date formats.

Objective

The objective is to identify and resolve common data quality issues and prepare the dataset for reliable analysis.

Tools Used

- Python
- Pandas
- VS Code

Data Quality Issues Identified

The following issues were identified in the raw dataset:

1. Missing values in the Name and Salary columns.
2. Missing values in the Joining_Date column.
3. Duplicate records.
4. Inconsistent Department formatting and whitespace.
5. Mixed date formats in the Joining_Date column.

Data Cleaning Approach

1. Missing Salary

The missing Salary value was replaced using the median salary of the available records.

2. Missing Name

The missing Name value was replaced with "Unknown".

3. Duplicate Records

Duplicate rows were identified and removed using Pandas "drop_duplicates()".

4. Department Standardization

Leading and trailing spaces were removed, and department names were converted to uppercase for consistency.

5. Date Standardization

The Joining_Date column was converted to a datetime format. Valid dates were standardized to a consistent date format.

6. Validation

After cleaning, the dataset was checked again for missing values, duplicate records, and data types.

Outcome

The raw dataset was successfully cleaned and prepared for analysis.

The final dataset contains:

- No duplicate rows.
- No missing values in Name, Department, or Salary.
- Standardized department names.
- Standardized Joining_Date values where valid.
- Missing joining dates are retained as "NaT" because the actual dates were unavailable.

The cleaned dataset was exported as "cleaned_dataset.csv".

How to Run

1. Install Python.
2. Install Pandas:
   "pip install pandas"
3. Run the Python script:
   "python day1_cleaning.py"
4. The cleaned dataset will be generated as:
   "cleaned_dataset.csv"

Project Files

- "day1_cleaning.py" – Python script used for data cleaning.
- "cleaned_dataset.csv" – Final cleaned dataset.
- "README.md" – Project documentation.