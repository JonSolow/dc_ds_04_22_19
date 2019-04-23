#!/usr/bin/env python
# coding: utf-8

# ### 1. Create a dictionary where each object contains a list of one float (Age) and one string (Family name) (at least 5 objects)

# In[20]:


AnimalDict = {'Chicken': [2.3, "Wings"], 'Cow': [3.4, "Steak"], 'Turkey': [5.3, "Turkey"], 'Duck': [4.5, "Confit"], 'Salmon': [0.2, "Salmon"]}


# ### 2. Delete one object from the dictionary

# In[21]:


AnimalDict.pop('Salmon')
AnimalDict


# ### 3. Replace the float number of one of your objects - we are changing a list entry inside a dictionary record! look at Darwin's new age
# 
# #Example:
# #`{Charles: [99.73, "Darwin"], Alan: [42.5, "Turing"]}`

# In[23]:


SearchString = 'Chicken'
ReplaceValue = 10.0
AnimalDict[SearchString][0]=ReplaceValue
AnimalDict


# ### 4. write a for loop that goes through all records in the dictionary, prints the family name and assigns the float numbers into one merged list (see ages)
# 
# `ages = [23.4, 22.9, 552.9]`

# In[26]:


ratings = []
for k, v in AnimalDict.items():
    print(k)
    ratings.append(v[0])
    


# ### 5. Download your notebbok as a .py (regular python script) save it somewhere you know

# ### 6. Go to terminal, navigate to the folder where you have saved the script and execute it through the terminal
# 
# `use commandds: 
# cd and 
# python your_script.py`

# ### [optional] Calculate with a for loop the median and mean of the ages list
