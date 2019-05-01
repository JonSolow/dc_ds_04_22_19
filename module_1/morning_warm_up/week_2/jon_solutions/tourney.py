#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# create your first simulation
### 1. Open the notebook about python fundmentals 
### 2. Add records to the dictionary until you have 24 names 
### 3. loop through the dictionary in pairs (pick two records at a time)
### 4. Use numpy random to throw a coin (virtual coin)
### 5. if heads delete first record, else delete second record 
### 6. continue till there is one winner 
### 7. print winner's name 
### 8. execute from terminal


# In[ ]:


# create your first simulation
### 1. Open the notebook about python fundmentals 


# In[ ]:


### 2. Add records to the dictionary until you have 24 names 


# In[21]:


import numpy as np


# In[65]:


names_as_text = """Solange Mance
Candra Roberie
Marielle Truman
Sebastian Troutman
Gaston Westman
Harold Takacs
Shavon Karr
Kymberly Quintanar
Ciara Washam
Marin Crittendon
Eleonora Henningsen
Ethel Thiele
Linnea Tweed
Maritza Moates
Rafaela Hester
Robyn Keeter
Gemma Maravilla
Stephine Reiner
Lynwood Cordeiro
Earnest Endres
Myron Issa
Niki Mealing
Kaylene Accardo
Haywood Mcmann
Huey Wilkerson
Magnolia Loveall
Joesph Southworth
King Cabaniss
Eugenie Perea
Dorie Maziarz"""

names_as_list = names_as_text.split('\n')
names_as_list

names_as_dict = {}

for names in names_as_list:
    if len(names_as_dict) < 24:
        names_as_dict.update({names: np.random.randint(25)})

names_as_dict
    


# In[66]:


# regenerating the list of names, which we only already had because of how we created the dictionary

names_as_list = []
for k, v in names_as_dict.items():
    names_as_list.append(k)

# initial round number
round_no = 1

# keep looping until 1 team remains
while len(names_as_dict) > 1:
    # print the current round number and number of teams
    print('Round Number: ', round_no)
    print(len(names_as_dict), ' teams remain \n')
    # keep track of how many have been removed in this round for adjusting indexing
    removed = 0
    # loop for the current number of names in this round
    for i in range(len(names_as_dict)):
        # first condition will make us skip over every other item
        # second condition handles cases where there are an odd number of teams remaining in that round
        if (i % 2 == 0) and (i+1-removed) < len(names_as_dict):
            # flip coin
            coinflip = np.random.randint(0, 1)
            # print the current matchup
            # note index is i - removed = first person
            print(names_as_list[i - removed], ' vs ',
                  names_as_list[i+1 - removed])
            # print the winner
            print(names_as_list[i - removed+(1-coinflip)], ' wins', '\n')
            # remove the loser from dictionary and list
            names_as_dict.pop(names_as_list[i - removed+coinflip])
            names_as_list.pop(i - removed+coinflip)
            # keep track of number removed
            removed += 1
    # advance round
    round_no += 1

