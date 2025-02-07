#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


file_name = "EDA/Books_Data_Clean.csv"


# In[7]:


df = pd.read_csv(file_name)


# In[8]:


df.head()


# In[9]:


rows, cols = df.shape
print(f"Number Of Rows : {rows}")
print(f"Number Of Cols: {cols}")


# In[10]:


df.describe()


# In[11]:


df.info()


# In[ ]:
