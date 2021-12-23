
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('Student-University(1).csv')


# In[3]:


data


# In[4]:


shuffle_data = data.sample(frac=1)
train_size = int(0.7 * len(data))
train_set = shuffle_data[:train_size]
test_set = shuffle_data[train_size:]


# In[6]:


X1_train=train_set['X1'].values
X2_train=train_set['X2'].values
y_train=train_set['Y'].values


# In[7]:


X1_train


# In[8]:


X2_train


# In[10]:


b0=0.1
b1=0.2
b2=0.3
epochs=1000
alpha=0.01
i=0

for i in range(epochs):
    for i in range(len(y_train)):
        y_hat=b0+b1*X1_train[i]+b2*X2_train[i]
        pred=1/(1+np.exp(-y_hat))
        b0=b0+alpha*(y_train[i]-pred)*pred*(1-pred)*1
        b1=b1+alpha*(y_train[i]-pred)*pred*(1-pred)*X1_train[i]
        b2=b2+alpha*(y_train[i]-pred)*pred*(1-pred)*X2_train[i]


# In[11]:


b0,b1,b2


# In[13]:


X1_train=train_set['X1'].values
X2_train=train_set['X2'].values
y_test=train_set['Y'].values

y=[]
print(y_train)
for i in range(len(y_test)):
    y_hat=b0+(b1*X1_train[i])+(b2*X2_train[i])
    pred=1/(1+np.exp(-y_hat))
    pred=int(pred)
    y.append(pred)
print(y)


# In[16]:


from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y))

