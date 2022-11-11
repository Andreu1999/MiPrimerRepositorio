#!/usr/bin/env python
# coding: utf-8

# Instal·lació paquet

# In[1]:


#!pip install palmerpenguins


# Importam pandas i fitxer

# In[1]:


import pandas as pd
from palmerpenguins import load_penguins #importamos la librería y el archivo


# In[2]:


penguins = load_penguins() #cargamos el archivo


# In[3]:


penguins #lo visualizamos


# In[4]:


penguins=penguins.dropna() #eliminamos los NA


# Comprovam que no hi ha NA

# In[5]:


print(penguins.isna().any()) #comprobamos si los hemos quitado bien


# In[6]:


bySex = penguins.groupby('sex') #agrupamos por sexo


# In[7]:


bySex.describe() #vemos el resultado


# In[8]:


penguins.insert(loc=8, column="bill_area", value=penguins.bill_length_mm*penguins.bill_depth_mm) #añadimos la nueva variable


# In[9]:


penguins #visualizamos el data modificado


# In[10]:


specsex = penguins.groupby(['sex',"species"]) #agrupamos por sexo y especie


# In[11]:


specsex.describe() #visualizamos el resultado


# In[39]:


penguins.insert(loc=9, column="body_mass_kg", value=penguins.body_mass_g/1000) #añadimos la nueva variable


# In[43]:


penguins=penguins.drop(columns=["body_mass_g"]) #eliminamos la variable antigua


# In[44]:


penguins #visualizamos el data actualizado

