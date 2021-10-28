
# coding: utf-8

# In[3]:


def mat():
    speed = input("enter the size of array")
    mean=0
    n=int(speed)
    for i in range(0,n):
        ele=int(input())
        mean=mean+ele
    print(mean)
    mean = mean/n
    print(mean)
mat()
        


# In[9]:


def median():
    m=input("enter the size of array")
    n=int(m)
    a=[]
    for i in range(0,n):
        ele=int(input())
        a.append(ele)
    a.sort()
    b=[]
    b=a
    index=len(b)//2
    
    if len(a)%2!=0:
        return b[index]
    else:
        return (b[index-1]+b[index])/2
median()


# In[20]:


from statistics import stdev
from statistics import variance
import numpy
from scipy import stats
m=input("enter the size of array")
n=int(m)
a=[]
for i in range(0,n):
    ele=int(input())
    a.append(ele)
l=numpy.mean(a)
k=numpy.median(a)
g=stats.mode(a)
print("standard devation of this set is %s :"%(stdev(a)))
print("variance of this set is %s:"%(statistics.variance(a)))
print("mean of this set is :",l)
print("median of this set is :",k)
print("mode of this set is :",g)

