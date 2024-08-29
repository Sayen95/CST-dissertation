#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the datasets
complete_renewable_energy_df = pd.read_csv("C:/Users/Sayen/OneDrive/Documents/CST PROJECT.60/complete_renewable_energy_dataset.csv")
global_renewable_energy_production_df = pd.read_csv("C:/Users/Sayen/OneDrive/Documents/CST PROJECT.60/global_renewable_energy_production.csv")
sustainable_energy_df = pd.read_csv("C:/Users/Sayen/OneDrive/Documents/CST PROJECT.60/global-data-on-sustainable-energy.csv")
# Check the first few rows of each dataset
print(complete_renewable_energy_df.head())
print(global_renewable_energy_production_df.head())
print(sustainable_energy_df.head())


# In[2]:


# Rename columns for consistency
complete_renewable_energy_df.rename(columns={'CO2 Emissions': 'CO2 Emissions (kt)', 'GDP': 'GDP (USD)'}, inplace=True)
sustainable_energy_df.rename(columns={'Entity': 'Country'}, inplace=True)


# In[5]:


# Drop rows where any values are missing
complete_renewable_energy_df = complete_renewable_energy_df.dropna(how='any')
global_renewable_energy_production_df = global_renewable_energy_production_df.dropna(how='any')
sustainable_energy_df = sustainable_energy_df.dropna(how='any')


# In[6]:


# Save the cleaned dataset
complete_renewable_energy_df.to_csv("C:/Users/Sayen/OneDrive/Documents/CST PROJECT.60/inprogress/complete_renewable_energy_df.csv", index=False)
global_renewable_energy_production_df.to_csv("C:/Users/Sayen/OneDrive/Documents/CST PROJECT.60/inprogress/global_renewable_energy_production_df.csv", index=False)
sustainable_energy_df.to_csv("C:/Users/Sayen/OneDrive/Documents/CST PROJECT.60/inprogress/sustainable_energy_df.csv", index=False)

