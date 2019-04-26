#!/usr/bin/env python
# coding: utf-8

# Pandas and numpy - pair-up
# Discussion session
# How will you read the following data into a pandas data frame ? ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt

# In[80]:


import pandas as pd
import numpy as np
df = pd.read_table("ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt", delim_whitespace=True, comment='#', header=None)
df.head()


# 2. How would you pick columns 0,1,3 ?  
# `[[0, 1, 3]]`

# In[81]:


df_013 = df.iloc[:,[0,1,3]]
df_013.head()


# 3. Use a for loop to find all rows where 
# Co2 (column 3) enteries with the value -99.99 (these are missing values) and replace them with NaN values (try using np.nan - do you know what it is? )

# In[69]:


for i in range(len(df_013)):
    if df_013[3][i] == -99.99: df_013[3][i] = np.nan
        
        


# 4. Change names of columns to year, month, and CO2 (use colnames)
# 

# In[70]:


my_columns = ["year", "month", "CO2"]
df_013.columns = my_columns
df_013.head()


# 5. Add a column 'Day' and specifiy the day 15 for all enteries

# In[71]:


df_013['day']=15
df_013.head()


# 6. Add a date column according to the 'year', 'month' and 'day' columns (options: use apply with lambda or for loop together with datetime.date (make sure to import it)) 

# In[72]:


#df_013['date'] = (str(df_013['month']+'-'+str(df_013['day'])+'-'+str(df_013['year']))  #.map(lambda x: x[:10])

df_013['date'] = list(map(lambda i: (str(df_013['month'][i])+'/'+str(df_013['day'][i])+'/'+str(df_013['year'][i])), range(len(df_013))))
df_013['date'] = pd.to_datetime(df_013['date'], format='%m/%d/%Y', errors = 'ignore')

df_013.head()
#range(len(df_013))


# 7. Drop the 'Day' column

# In[73]:


df_013.drop(columns='day', inplace = True)


# In[74]:


df_013.head()


# 8. use pandas groupby to print the yearly avg. of co2 per year. 

# In[75]:


df_013.groupby('year').CO2.sum()


# 9. Pick columns that you think could be used to build a model and store them in numpy array (Answer why do we do that?)
# 

# In[79]:


co2_arr = np.asarray(df_013.CO2)
co2_arr


# 10. repeat step (3) but this time using the np.where command. 

# In[93]:


#3. Use a for loop to find all rows where 
#Co2 (column 3) enteries with the value -99.99 (these are missing values) and 
#replace them with NaN values (try using np.nan - do you know what it is?)

df_013 = df.iloc[:,[0,1,3]]

print(df_013[:8])

print('\n')
df_013[3] = np.where(df_013[3] == -99.99, np.nan, df_013[3])

print(df_013[:8])


# 11. Download the notebook as .py script and run it from your terminal. 

# In[ ]:





# 12. Create a branch in github repository called warm_up_draft   

# In[ ]:





# 13. push the notebook with the name CO2 to your new branch on github.

# In[ ]:




