#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[13]:


data=pd.read_csv('myexcel - myexcel.csv.csv')
data


# In[14]:


data.isnull().sum()


# In[25]:


x = data['Salary'].mean()
data['Salary'].fillna(x,inplace = True)
data


# In[26]:


data.drop_duplicates(inplace = True)
data


# In[27]:


data.dropna (inplace = True)


# In[28]:


data.isnull().sum()


# In[29]:


data['Height'] = np.random.uniform(150,180,size = len(data))


# In[30]:


data


# # How many are there in each team and percentage splitting with respect to the total employees
# 

# In[31]:


data['Team'].value_counts()


# # Percentage splitting with respect to the total employees

# In[32]:


data['Team'].value_counts()/len(data)*100


# # Segregate the employees w.r.t different positions

# In[35]:


employees = data.groupby('Position')['Name'].apply(list)
for Position, Names in employees.items():
    print(f"employees in {Position} position:")
    for name in Names:
        print(name)
        print("\n")


# # Find from which age group most of the employees belong to.

# In[36]:


data['Age Group'] = data['Age'].apply(lambda age:'20-25' if 20 <= age <=25 else ('26-30'if 26 <= age <= 30 else ('31-35' if 31 <= age <= 35 else '36 and above')))
data


# In[37]:


data['Age Group'].value_counts()


# # Find out under which team and position, spending in terms of salary is high

# In[40]:


spending_salary = data.groupby(['Team','Position'])['Salary'].sum()
spending_salary.idxmax()


# # Find if there is any correlation between age and salary,represent it visually.

# In[41]:


correlation = data['Salary'].corr(data['Age'])


# In[42]:


print("THE CORRELATION B/w Salary AND IS:",correlation)


# In[43]:


sns.scatterplot(x="Age" ,y= "Salary",data= data)
plt.ylabel("Salary")
plt.xlabel("Age")
plt.title("correlation b/w Salary and Age")
plt.show()


# In[ ]:




