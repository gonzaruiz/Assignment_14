
# coding: utf-8

# In[50]:



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')

from pandas import DataFrame, Series
import sqlite3 as db
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

sqladb = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", names=[
    'age','workclass','fnlwgt','education','education-num','marital-status','occupation', 
    'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','x'])
sqladb


# In[51]:


df = sqladb
df.head(2)


# In[52]:


df.info()


# In[53]:


list(df.index)


# In[54]:


df.index.values


# In[55]:


df.columns


# In[56]:


pysqldf("""SELECT * FROM sqladb LIMIT 10 """)


# In[57]:


sqladb['hours-per-week'] = pd.to_numeric(sqladb['hours-per-week'])
sqladb['hours-per-week']
pysqldf("""SELECT workclass, MAX("sqladb.hours-per-week") FROM sqladb 
            WHERE sex NOT LIKE '%Female%' 
            GROUP BY workclass; """)


# In[58]:


df.sort_values('sex')


# In[59]:


df.sort_values(['education','race'])


# In[60]:


df[['age','workclass','fnlwgt','education','education-num','marital-status','occupation', 
    'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','x']]


# In[61]:


df.loc[[11,24,37]]


# In[62]:


lista_indices = list(range(0,5)) + list(range(6,12)) + list(range(13,23)) + list(range(24,56)) + list(range(57, 4656))
df.loc[lista_indices]


# In[63]:


nombre = "sex"
df[nombre].values


# In[64]:


from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)


# In[65]:


from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)

addresses = Table('addresses', metadata,
  Column('id', Integer, primary_key=True),
  Column('user_id', None, ForeignKey('users.id')),
  Column('email_address', String, nullable=False)
 )

