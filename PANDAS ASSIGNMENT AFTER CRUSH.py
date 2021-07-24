#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


#impor pandas
import pandas as pd


# In[3]:


#write a code to load the alumni csv dataset into a pandas DataFrame called "Alumni"
Alumni = pd.read_csv(r"C:\Users\Bala\Documents\ADS-Assignment-1-main\alumni.csv")
print(Alumni)


# In[28]:


#create a copy of the original data for ease of manipulation
Alumni_copied =Alumni.copy()


# In[29]:


#use the command "head" to understand the data
Alumni_copied.head()


# In[30]:


#use the command "tail" to understand the data
Alumni_copied.tail()


# In[31]:


#use the command "dtypes" to understand the data
Alumni_copied.dtypes


# In[32]:


#use the command "info" to understand the data
Alumni_copied.info()


# In[33]:


#use the command "describe" to understand the data
Alumni_copied.describe()


# In[34]:


#create a "Savings"column derived from Savings($)
Alumni_copied["Savings"] =Alumni_copied["Savings ($)"]


# In[35]:


#run the commd Alumni.head to confirm if the new "Savings" column has been created
Alumni_copied.head()


# In[54]:


#check on the data type for "savings" column ad how many they are incase they are diferrent types
Alumni_copied["Savings"].apply(type)


# In[51]:


#using the "clean currency", clean up the string and remove the special characters on "Savings" and convert to float since they are strings 
Alumni_copied["Savings"] = Alumni_copied["Savings"].str.replace(',','').str.replace('$','').astype('float')


# In[53]:


#check the type of change that has occured ie the class has changed from "string" to "float"
Alumni_copied["Savings"].apply(type)


# In[65]:


#Run the "Alumni" ["Gender"].value_counts to se the incorrect "M" that need to be convered to "Male"- count is 3
Alumni_copied["Gender"].value_counts()


# In[68]:


#Check the data type for the Gender column-Are all strings
Alumni_copied["Gender"].apply(type)


# In[63]:


#Replace the incorrecct data "M" with "Male" in the gender column. use (^...$) to restrict the pattern to match the whole string
Alumni_copied.replace({"Gender": r"^M.$"}, {"Gender": "Male"}, regex=True)


# In[69]:


#Check datatype after conveting "M" to "Male"
Alumni_copied["Gender"].apply(type)


# In[71]:


#Set the change from "M" to "Male" after using the df.loc command
Alumni_copied.loc[Alumni_copied["Gender"] =="M"] = "Male"


# In[88]:


#Run the "Gender" value count to confirm if the change has been effected[Threare n0 more"M"
Alumni_copied["Gender"].value_counts()


# In[93]:


#Get the "median" for the salary coumn
Alumni_copied["Salary"].mean()


# In[94]:


#Get the mean of Salary column
Alumni["Salary"].Mean()


# In[95]:


#Get the standard deviation
Alumni_copied["Salary"].std()


# In[96]:


#Get the satndard deviation using the loc for comparison
Alumni_copied.loc[:,"Salary"].std()


# In[97]:


#Get the median using the loc for comparison
Alumni_copied.loc[:,"Salary"].median()


# In[ ]:




