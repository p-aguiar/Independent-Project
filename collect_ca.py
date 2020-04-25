#Step 1: Pull Population and Demographic Data from the Census using an api 
#%% 1- Import modules 
import requests
import pandas as pd 
#%% 2- Use census-data.csv to refine api search 
refine= pd.read_csv('census-data.csv')
#%% 3- set var_name to variable column in csv and cover to list 
name= refine['Variable'].to_list()
#%% 4- set var_list to Name to return the official location names
var_list = ['NAME']+name
#%%5- join the var_list and create a string variable 
var_string = ','.join(var_list)
#%%6-Call address for API
api = 'https://api.census.gov/data/2018/acs/acs5' 
#%%7- set for_clause to counties
for_clause= 'county:*'
#%% 8-set in_clause to California
in_clause= 'state:06'
#%%9- set key value (use personal key)
key_value = 'ec96ba98e74c748a196d1eb949df3ef8c6e87242'
#%% 10-set payload
payload = {'get':var_string, 'for':for_clause, 'in':in_clause,'key':key_value}
#%% 11 -set response to build query string
response = requests.get(api, payload)
#%% 12 - use .json command to return a list of rows
row_list = response.json()
#%% 13 - set column names
colnames =row_list[0]
#%% 14- set datarows 
datarows = row_list[1:]
#%% 15- covert data into a panadas dataframe 
ca_data = pd.DataFrame(columns=colnames, data=datarows)
#%% 16- set the dataframe index to names
ca_data.index('NAME', inplace=True)
#%% 16-outwrite repsonses to new csv 
ca_data.to_csv('census-data-ca.csv')