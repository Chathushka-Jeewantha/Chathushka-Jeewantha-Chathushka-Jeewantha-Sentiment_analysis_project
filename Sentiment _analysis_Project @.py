#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("sentiment_analysis[1].csv")
data.head()


# In[3]:


data.shape


# In[4]:


data.duplicated().sum()


# In[5]:


data.isnull().sum()


# In[ ]:




