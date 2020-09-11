#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-2 Day-5

# In[3]:


for i in range(1,2500):
    count = 0
    for j in range(1,i+1):
        if(i%j==0):
            count = count + 1
    if(count==2):
        print(i)


# In[ ]:




