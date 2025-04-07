#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd 


# # Step 1: Load the dataset

# In[19]:


df = pd.read_csv("marketing_campaign.csv", sep = "\t")
df


# In[20]:


df.head()


# # Step 2: Remove duplicate rows

# In[21]:


df = df.drop_duplicates()


# # Step 3: Handle missing values using

# In[23]:


print(df.isnull().sum())


# In[ ]:


# Fill missing values in 'Income' with median
income_median = df['Income'].median()
df['Income'].fillna(income_median, inplace=True)


# # Step 4: Standardize text values

# In[24]:


# Strip spaces and make first letter uppercase (Title Case)
df['Education'] = df['Education'].str.strip().str.title()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.title()


# # Step 5: Convert date column to datetime

# In[25]:


# Convert Dt_Customer to datetime (day-first format)
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], dayfirst=True)


# # Step 6: Rename column headers to be lowercase and snake_case

# In[26]:


# Rename columns: lowercase + underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


# # Step 7: Fix data types

# In[27]:


# Make sure data types are correct
df['year_birth'] = df['year_birth'].astype(int)
df['income'] = df['income'].astype(float)


# In[28]:


df


# Summary of Data Cleaning
# Removed duplicates
# → Ensured no repeated rows.
# 
# Handled missing values
# → Filled 24 missing Income values using the column’s median.
# 
# Standardized text
# → Cleaned and formatted values in Education and Marital_Status (e.g., proper casing, no extra spaces).
# 
# Converted date format
# → Changed Dt_Customer to proper datetime type using dd-mm-yyyy.
# 
# Renamed columns
# → Made all column names lowercase and replaced spaces with underscores (e.g., Year_Birth → year_birth).
# 
# Fixed data types
# → Converted year_birth to int and income to float.

# In[ ]:




