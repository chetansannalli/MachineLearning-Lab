
# coding: utf-8

# In[1]:


print("ch")


# In[2]:


num1=20
num2=10
sum=num1+num2
print(sum)


# In[10]:


num=int(input("enter the number"))
if (num/2)==0:
    print("the number is even")
else:
    print("the number is odd")


# In[2]:


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select operators")
print("1.Add")
print("2.substract")
print("3.multiply")
print("4.divide")
while True:
    choice=input("enter the choice")
    if choice in('1','2','3','4'): 
        num1=float(input("enter the number"))
        num2=float(input("enter the number"))
        if choice=='1':
            num2 = add(num1,num2)
            print(num2)
        elif choice=='2':
            num2 = sub(num1,num2)
            print(num2)
        elif choice=='3':
            num2 = mul(num1,num2)
            print(num2)
        elif choice=='4':
            num2 = div(num1,num2)
            print(num2)
        next_calculation=input("do you want to continue?: (yes/no):")
        if next_calculation== "no":
            break
    else:
        print("invalid input")
    


# In[3]:


list=["nitte","meenakshi","institute"]
list1=["NMIT","yelahanka","bengaluru"]
print(list)


# In[4]:


print(list1)


# In[5]:


print(list+list1)


# In[6]:


list[1::3]


# In[8]:


list1[0::2]


# In[9]:


list1[0::2]


# In[10]:


list[0::1]


# In[11]:


list[0:3]


# In[12]:


list[0:2]


# In[20]:


print(list)


# In[21]:


list.append("abc")
print(list)


# In[22]:


list.append("bcd")


# In[23]:


print(list)


# In[24]:


list.pop()


# In[25]:


list.pop()


# In[26]:


print(list)


# In[28]:


list.extend([4,5])


# In[29]:


print(list)


# In[30]:


list.index("meenakshi")


# In[31]:


order=("rice","dal","cooldrink")
print(order)


# In[32]:


print(len(order))


# In[33]:


list[1]="Meenakshi"


# In[34]:


print(list)


# In[35]:


order.append("roti")


# In[36]:


print(type(order))


# In[47]:


cars={"brand":"ford","model":"mustang","year":"1976"}


# In[38]:


print(cars)


# In[48]:


print(cars["brand"])


# In[49]:


print(len(cars))


# In[50]:


cars["brand"]="benz"


# In[51]:


print(cars)

