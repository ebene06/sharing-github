#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

arr = [6, 7, 8, 9]
print(type(arr))


# In[3]:


a =  np.array(arr)
print(type(a))
print(a.shape)
print(a.dtype)


# In[6]:


#get the dimension of a with ndim
print(a.ndim)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)


# In[9]:


# a 2x3 array with random values
np.random.random((2, 3))


# In[10]:


#a 2x3 array of zeros
np.zeros((2, 3))


# In[11]:


#a 2x3 array of ones
np.ones((2, 3))


# In[18]:


#a 3x3 identity matrix
np.zeros((3, 3, 3))


# In[20]:


c = np.array([[9.0, 8.0, 7.0], [1.0, 2.0, 3.0]])
d = np.array([[4.0, 5.0, 6.0], [9.0, 8.0, 7.0]])

c + d


# In[21]:


c = np.array([[9.0, 8.0, 7.0], [1.0, 2.0, 3.0]])
d = np.array([[4.0, 5.0, 6.0], [9.0, 8.0, 7.0]])

c * d


# In[23]:


c = np.array([[9.0, 8.0, 7.0], [1.0, 2.0, 3.0]])
d = np.array([[4.0, 5.0, 6.0], [9.0, 8.0, 7.0]])

5/d


# In[24]:


c = np.array([[9.0, 8.0, 7.0], [1.0, 2.0, 3.0]])
d = np.array([[4.0, 5.0, 6.0], [9.0, 8.0, 7.0]])

c ** 2


# In[25]:


a[0]


# In[26]:


d[1, 0:2]


# In[27]:


e = np.array([[10, 11, 12], [13, 14, 15],
             [16, 17, 18], [19, 20, 21]])

#slicing
e[:3, :2]


# In[28]:


e[[2, 0, 3, 1], [2, 1, 0, 2]]


# In[29]:


e[e>15]


# In[ ]:




