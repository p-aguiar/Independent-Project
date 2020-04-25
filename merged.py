#4 -Join ca-covid.csv to ca-high-risk-pop.csv
#%% 1- import modules
import pandas as pd 
#%% 2- import csvs
covid = pd.read_csv('ca-covid.csv')
ca = pd.read_csv('ca-high-risk-pop.csv')
#%% 3 - merge data sets 
merged = covid.merge(ca, on='county')
#%% 4- export to cvs 
merged.to_csv('merged.csv', index=False)