#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Installing Pandas and os 

import pandas as pd
import os

# Importing Data Frame 
df = pd.read_excel(r"C:\Users\k4leu\OneDrive\Documents\white_belts_3.25.xlsx")

# Data Fram Overview 
print(df)


# In[4]:


# Data Frame objects

df.info()


# In[6]:


# Checking Initial statistics for Data Frame 

df.describe()


# In[3]:


# Creating data subset of all Poomsae scores. 

psae_scores = df[['Kicho 1 and 2', 'Stances', 'Blocks', 'Hand Strikes', 'Poomsae Kicks']]
psae_scores


# In[4]:


# Finding the average score of 'Kicho 1 and 2' Patterns and Components
# Creating a Data Frame with averages

psae_avr = pd.DataFrame(psae_scores.mean(), columns = ['Avg'])
psae_avr.index.name = 'psae Components'
psae_avr


# In[7]:


#Finding Lowest average is 3.7 - Stances 

psae_avr.idxmin()
psae_avr.min()


# In[36]:


# Finding Highest average is 4.1 - Poomsae Kicks

psae_avr.max() 


# In[53]:


# Creating a Column Graph of the Psae Data Frame

psae_avr.plot(kind='barh', figsize=(10,5))


# In[8]:


# Creating a subset of all kicking scores that are not related to Poomsae 

kick_score = df[[ 'High-Rising', 'Out-In','In-Out', 'Roundhouse', 'Front', 'Kick AVG',]]


# In[9]:


# Finding average kick scores and creating a data frame with averages

kick_avr = pd.DataFrame(kick_score.mean(), columns=['Avg'])
kick_avr.index.name='Kick Type'
kick_avr


# In[11]:


# Finding Lowest average kick is the Inside-Outside Crescent Kick

kick_avr.min()


# In[12]:


# Finding Highest Average kick score is the Front Kick

kick_avr.max()


# In[13]:


# Creating a Column Chart with the kick_avr Data Frame

kick_avr.plot(kind='barh', figsize=(10,5))


# In[92]:


# Exporting psae_avr and kick_avr to Excel and into Tableau
    
path = os.path.join(os.path.expanduser("~"), "Documents", r"C:\Users\k4leu\OneDrive\Documents\BELT TESTING DATA")
kick_avr.to_csv(os.path.join(path, 'kick_avr.csv'), index = True)

path = os.path.join(os.path.expanduser("~"), "Documents", r"C:\Users\k4leu\OneDrive\Documents\BELT TESTING DATA")
psae_avr.to_csv(os.path.join(path, 'psae.csv'), index = True)


# In[ ]:





# In[ ]:




