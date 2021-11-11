
# coding: utf-8

# In[31]:


import pandas as pd
data = pd.read_csv("c1.csv")
data


# In[32]:


point_1=[6.2,3.2]
point_2=[6.6,3.7]
point_3=[6.5,3.0]
point_1,point_2,point_3


# In[33]:


import math as m
c1=[]
c2=[]
c3=[]
def ecul(x,y):
    d1=m.sqrt((point_1[0]-x)**2 + (point_1[1]-y)**2)
    d2=m.sqrt((point_2[0]-x)**2 + (point_2[1]-y)**2)
    d3=m.sqrt((point_3[0]-x)**2 + (point_3[1]-y)**2)
    md=min(d1,d2,d3)
    if md == d1:
        c1.append([x,y])
    elif md == d2:
        c2.append([x,y])
    elif md == d3:
        c3.append([x,y])
for i in range(0,10):
    ecul(data['x'][i],data['y'][i])
print("cluster_1 : ",c1)
print("cluster_2 : ",c2)
print("cluster_3 : ",c3)


# In[34]:


c1=[((x[0]+x[1]+x[3])/3),((y[0]+y[1]+y[2])/3)]
print(c2)


# In[ ]:


c

