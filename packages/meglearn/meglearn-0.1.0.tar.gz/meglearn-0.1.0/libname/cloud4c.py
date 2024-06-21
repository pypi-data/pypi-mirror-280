#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Cloud4c:
    def __init__(self,name):
        self.name=name
        print(name)
    def change_name(self,name):
        self.name=name
        print(self.name)


# In[7]:


c=Cloud4c("meg")
c.change_name("sai")


# In[ ]:




