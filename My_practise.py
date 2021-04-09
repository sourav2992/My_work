#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data_BM= pd.read_csv("E:/My_pythone _practise/Pandas Part 1/bigmart_data.csv")


# In[3]:


data_BM.head()


# In[4]:


data_BM.isna().values.any()


# In[13]:


data_BM.isna().sum()


# In[12]:


data_BM["Outlet_Size"].isna().sum()


# In[10]:


data_BM=data_BM.dropna(how="any")


# In[15]:


data_BM.shape


# In[16]:


data_BM.sort_values("Outlet_Establishment_Year",ascending=False)


# In[17]:


data_BM= data_BM.reset_index(drop=True)


# In[18]:


data_BM.head()


# In[36]:


price_by_item = data_BM.groupby("Item_Type")
price_by_item.first()


# In[37]:


price_by_item.Item_MRP.mean()


# In[39]:


pd.crosstab(data_BM["Outlet_Size"],data_BM["Outlet_Location_Type"],margins=True)


# In[40]:


pd.pivot_table(data_BM,index="Outlet_Establishment_Year",values="Item_Outlet_Sales")


# In[41]:


pd.pivot_table(data_BM,index=["Outlet_Establishment_Year","Outlet_Size","Outlet_Location_Type"],values="Item_Outlet_Sales")


# In[43]:


pd.pivot_table(data_BM,index=["Outlet_Establishment_Year","Outlet_Size","Outlet_Location_Type"],values="Item_Outlet_Sales",aggfunc=[np.mean,np.median,max,min,np.std])


# In[ ]:




