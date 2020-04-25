# Step 2 - Data Analysis on Population information collected from Census
##% 1 - import modules 
import pandas as pd 
#%% 2- set display parameters 
pd.set_option('display.max_rows',None)
#%% 3- import census-data.csv and set it to a variable
analyze= pd.read_csv('census-data.csv', index_col='Variable')
#%% 4- group variables and print to see groups 
group=analyze['Group']
print(group)
#%% 5 - Open census-data-ca and set index to Names 
health = pd.read_csv('census-data-ca.csv', index_col='NAME')
#%% 6 - Group by age 
group_by = health.groupby(group,axis='columns',sort=False)
#%%7 -Sum group_by and set to risk
by_risk = group_by.sum()
#%% 8 - Create risk list 
risk = ['total', 'total median age', 'male', 'female', 'male 60 to 61',
        'male 62 to 64', 'male 65 to 66', 'male 67 to 69', 'male 70 to 74',
        'male 75 to 79', 'male 80 to 84', 'male 85+',  'female 60 to 61', 'female 62 to 64', 
        'female 65 to 66', 'female 67 to 69', 'female 70 to 74',
        'female 75 to 79', 'female 80 to 84', 'female 85+']
#%% 9-print by_risk
print(by_risk)
#%% 10- Counties with the oldest population 
med_age= by_risk['total median age']
print('Counties from lowest to highest Median Age:' , med_age.sort_values())
med_age_male = by_risk['male']
print('Counties from lowest to highest Median Age of Men:',med_age_male.sort_values())
med_age_female= by_risk['female']
print('Counties from lowest to highest Median Age of Women:',med_age_female.sort_values())
#%% 11 - high risk male group 
high_risk_age_male=( by_risk['male 60 to 61']+by_risk['male 62 to 64']+
by_risk['male 65 to 66']+ by_risk['male 67 to 69']+ by_risk['male 70 to 74']
+by_risk['male 75 to 79']+by_risk['male 80 to 84']+by_risk['male 85+'])
by_risk['high risk males']=high_risk_age_male
hi_ratio_male=(round(high_risk_age_male/by_risk['total']*100,2))
by_risk['ratio high risk males']=hi_ratio_male
#%% 12 - high risk female group
high_risk_age_female=( by_risk['female 60 to 61']+by_risk['female 62 to 64']+
by_risk['female 65 to 66']+ by_risk['female 67 to 69']+ by_risk['female 70 to 74']
+by_risk['female 75 to 79']+by_risk['female 80 to 84']+by_risk['female 85+'])
by_risk['high risk females']=high_risk_age_female
hi_ratio_female=(round(high_risk_age_female/by_risk['total']*100,2))
by_risk['ratio high risk females']=hi_ratio_female
#%% 13- total high risk group 
high_risk_age= high_risk_age_female + high_risk_age_male
print('Total Population at risk:',high_risk_age)
by_risk['high risk total'] = high_risk_age
hi_ratio=(round(high_risk_age/by_risk['total']*100,2))
by_risk['total high risk ratio']= hi_ratio
print('Ratio of high risk individuals to total population:',hi_ratio.sort_values())
#%% 14-highest risk group (age 85+)
highest_risk_male = by_risk['male 85+']
by_risk['highest risk male'] = highest_risk_male

highest_ratio_male = (round(highest_risk_male/by_risk['total']*100,2))

by_risk['highest risk ratio male']=highest_ratio_male
highest_risk_female = by_risk['female 85+']

by_risk['highest risk female']=highest_risk_female
highest_ratio_female = (round(highest_risk_female/by_risk['total']*100,2))
by_risk['highest risk ratio female']=highest_ratio_female

highest_risk= by_risk['male 85+'] + by_risk['female 85+']
by_risk['highest risk total']=highest_risk

highest_ratio = (round(highest_risk/by_risk['total']*100,2))
by_risk['highest risk ratio']=highest_ratio
print('Counties with the greatest percentage of population with the highest risk:',highest_ratio.sort_values())
#%% 15 - Add county column 
county_list = ['Lake', 'Mariposa', 'Yuba','Contra', 'Lassen', 'Santa Barbara',
               'Sonoma', 'Imperial', 'Mono', 'Alameda', 'Sacramento', 'Napa', 
               'Monterey', 'Sierra', 'San Diego', 'Yolo', 'Humboldt', 'Alpine',
               'Mendocino','Santa Cruz', 'Los Angeles', 'Riverside', 'Santa Clara',
               'Marin', 'Siskiyou', 'Shasta','Del Norte', 'San Luis Obispo',
               'Glenn','Butte ', 'Plumas ','Kern','Orange', 'Calaveras',
               'Sutter','San Mateo','Tuolumne','San Joaquin','Amador',
               'Merced','Modoc','Inyo','Stanislaus', 'Tehama','San Benito',
               'El Dorado', 'San Francisco', 'Tulare','Nevada','Madera','Trinity',
               'San Bernardino','Placer', 'Solano', 'Colusa','Kings',
               'Fresno','Ventura']
by_risk['county']= county_list 
#%% 17 - Export to a CVS
by_risk.to_csv('ca-high-risk-pop.csv')