# Customer-Personality-Analysis
Customer Personality Analysis is a detailed analysis of a company’s ideal customers. It helps a business to better understand its customers and makes it easier for them to modify products according to the specific needs, behaviors and concerns of different types of customers.

Summary of Data Cleaning Removed duplicates → Ensured no repeated rows.

Handled missing values → Filled 24 missing Income values using the column’s median.

Standardized text → Cleaned and formatted values in Education and Marital_Status (e.g., proper casing, no extra spaces).

Converted date format → Changed Dt_Customer to proper datetime type using dd-mm-yyyy.

Renamed columns → Made all column names lowercase and replaced spaces with underscores (e.g., Year_Birth → year_birth).

Fixed data types → Converted year_birth to int and income to float.
