#!/usr/bin/env python
# coding: utf-8

# In[1]:


#conversion to csv
import pandas as pd
fuel_data = pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv')
fuel_data.to_csv('fuel_ferc1.csv', index=False)


# In[2]:


#reading data and description
import pandas as pd
fuel_data = pd.read_csv('fuel_ferc1.csv')
fuel_data.describe(include='all')


# In[3]:


#check for missing values
fuel_data.isnull().sum()


# In[4]:


#use groupby to count the sum of each unique value in the fuel unit column
fuel_data.groupby('fuel_unit')['fuel_unit'].count()
fuel_data[['fuel_unit']] = fuel_data[['fuel_unit']].fillna(value='mcf')


# In[5]:


#check if missing values have been filled
fuel_data.isnull().sum()

fuel_data.groupby('report_year')['report_year'].count()


# In[6]:


#group by the fuel type code year and print the first entries in all the groups formed

fuel_data.groupby('fuel_type_code_pudl').first()


# In[9]:


fuel_df1 = fuel_data.iloc[0:1900].reset_index(drop=True)
fuel_df2 = fuel_data.iloc[1900:].reset_index(drop=True)


# In[11]:


#check that the length of both dataframes sum to the expected length
assert len(fuel_data) == (len(fuel_df1) + len(fuel_df2))


# In[12]:


#outer merge returns all rows in both dataframes
pd.merge(fuel_df1, fuel_df2, how="inner")


# In[13]:


#outer merge returns all rows in both dataframes
pd.merge(fuel_df1, fuel_df2, how="outer")


# In[14]:


#removes rows from the right dataframe that don not have a match with the left
#and keeps all rows from the left
pd.merge(fuel_df1, fuel_df2, how="left")


# In[15]:


#check for duplicate rows
fuel_data.duplicated().any()


# In[17]:


#Import plotting library
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(7,4))
plt.xticks(rotation=90)
fuel_unit = pd.DataFrame({'unit':['BBL', 'GAL', 'GRAMSU', 'KGU', 'MCF', 'MMBTU', 'MWDTH', 'MWHTH', 'TON'],
                          'count':[7998, 84, 464, 110, 11354, 180, 95, 100, 8958]
                                          })
                        
sns.barplot(data=fuel_unit, x='unit', y='count')
plt.xlabel('Fuel Unit'),

#Because of the extreme range of the values for the fuel unit, we can plot the barchart by taking the logarithm of the y-axis as follows:
g = sns.barplot(data=fuel_unit, x='unit', y='count')
g.set_yscale("log")
g.set_ylim(1, 12000)
plt.xlabel('Fuel Unit'),


# In[34]:


import pandas as pd
# Import plotting library
import seaborn as sns
fuel_data =  pd.read_csv('fuel_ferc1.csv')

# Box plot
sns.boxplot(x="fuel_type_code_pudl", y="utility_id_ferc1",
            palette=["m", "g"], data=fuel_data)


# In[7]:


# Select a sample of the dataset
sample_df = fuel_data.sample(n=50, random_state=4)
sns.regplot(x=sample_df["utility_id_ferc1"], y=sample_df["fuel_cost_per_mmbtu"], fit_reg=False)


# In[5]:

#KDE Plotting
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fuel_data = pd.read_csv('fuel_ferc1.csv')
sample_df = pd.DataFrame(fuel_data.sample(n=50, random_state=7), columns=['fuel_cost_per_unit_burned'])


sns.kdeplot(sample_df['fuel_cost_per_unit_burned'], shade=True, color="b")
plt.xlabel('sample_df')


# In[ ]:




