#Step 3- Clean up COVID-19 Data 
#%% 1- import modules 
import pandas as pd 
#%% 2 - import county data csv
county = pd.read_csv('us-counties.csv',index_col='state')
#%% 3- drop all non-california observations 
county = county.loc['California']
#%% 4- Remove all dates except most recent
county =county.query('date == "4/18/20"')
#%%5- export to csv
county.to_csv('ca-covid.csv')
