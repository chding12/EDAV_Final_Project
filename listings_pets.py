
# coding: utf-8

# In[126]:

import pandas as pd


# In[135]:

listings = pd.read_csv('cleaned_data.csv')


# In[136]:

listings['amenities'] = listings['amenities'].apply(lambda x: x.replace('{','').replace('}','').replace('\"','').replace('/',' ').replace('’','').replace(',',' ').lower())


# In[137]:

listings.to_csv('listings_pets.csv')

