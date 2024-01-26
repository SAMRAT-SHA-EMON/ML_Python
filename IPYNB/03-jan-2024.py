#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_excel("RFM.xlsx")


# In[2]:


data


# In[3]:


data.head(5)


# In[4]:


data.shape


# In[5]:


data.local_caller_time = data.local_caller_time.map(lambda x: int(x))


# In[6]:


data


# In[7]:


data.size


# In[8]:


data.describe()


# In[9]:


(data == 0).any()


# In[10]:


index1 = (data['age'] == 0) | (data['gender'] == 0 )
index2 = (data['pay_num'] == 0) | (data['pay_times'] == 0 )


# In[11]:


index1


# In[12]:


data = data.drop(data[index1].index)
data.shape


# In[13]:


data


# In[14]:


index2


# In[15]:


data = data.drop(data[index2].index)
data.shape


# In[16]:


data


# In[17]:


data = data.drop_duplicates('user_id')


# In[18]:


data.shape


# In[19]:


data


# In[20]:


from datetime import datetime
start_time = datetime(2000,6,15)
end_time = datetime(2024,1,3)


# In[21]:


end_time


# In[22]:


start_time


# In[23]:


end_time - start_time


# In[24]:


data['last_pay_time'] = pd.to_datetime(data['last_pay_time'])


# In[25]:


data['last_pay_time']


# In[26]:


data['day'] = data['last_pay_time'] - start_time


# In[27]:


data.head(5)


# In[28]:


data.columns


# In[29]:


data = data.drop(['gender',
       'last_month_traffic', 'local_trafffic_month', 'local_caller_time',
       'service1_caller_time', 'service2_caller_time', 'online_time','age'], axis =1 )


# In[30]:


data.head(5)


# In[31]:


from math import ceil

day = data['last_pay_time'] - start_time

month = []

for i in day:
    month.append(ceil(float(i.days)/30.0))


# In[36]:


months = []

for i in month:
    if i == 0:
        months.append(1)
    else:
        months.append(i)


# In[37]:


months


# In[38]:


data['F']= data['pay_times']/months
data['M'] = data['pay_num']/months
data['R'] = end_time - data['last_pay_time'] 


# In[39]:


data1 = data[['user_id','R','F','M']]
data1['R'].mean()
data1['R'].std()
data1['R'] = data1['R'].map(lambda x: (x  - data1['R'].mean())/data1['R'].std())
data1['F'] = data1['F'].map(lambda x: (x  - data1['F'].mean())/data1['F'].std())
data1['M'] = data1['M'].map(lambda x: (x  - data1['M'].mean())/data1['M'].std())


# In[40]:


data1


# In[42]:


data1.to_csv('/Users/MONIRUL ISLAM/Desktop/shamrat/RFM.csv')


# In[43]:


data1.to_excel('/Users/MONIRUL ISLAM/Desktop/shamrat/RFM.xlsx')


# In[ ]:




