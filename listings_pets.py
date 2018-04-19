
# coding: utf-8

# In[126]:

import pandas as pd


# In[146]:

listings = pd.read_csv('cleaned_data.csv')
listings = listings[['id','neighbourhood_group_cleansed','amenities']]


# In[147]:

listings['amenities'] = listings['amenities'].apply(lambda x: x.replace('{','').replace('}','').replace('\"','').replace('/',' ').replace('’','').replace(',',' ').lower())


# In[148]:

listings.to_csv('listings_pets.csv')


# In[ ]:



