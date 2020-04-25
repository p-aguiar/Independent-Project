# Independent-Project

## Purpose of Analysis
The purpose of this analysis is to determine if localities with a higher proportion of at risk populations are more susceptible to the novel Corona Virus. This analysis will focus on one high risk group, people over 60 years of age, in the state of California. Obviously this is a simple analysis of a single state and single variable, there are other factors that influence the number of COVID-19 cases and deaths. However, this analysis does provide an interesting look at where in California risks might be greater.
## How to Conduct Analysis
The following steps will provide the necessary information to complete the analysis using Spyder. The deliverables will be a number of python scripts, .csv files and data visualizations.

### Step 1 - Pull Data from Census
This step obtains and edits the necessary demographic data for California.
1. Download census-data.csv from google drive (https://drive.google.com/drive/folders/1DxwNO3miY-rO5ipXEu-CIWJsmX4ViY0K?usp=sharing) to obtain a paired down list of relevant census data variables that will be useful in later scripts.
2. Open a new python script in Spyder called 'collect-ca.py. Import the requests module and import the pandas module as pd to read census-data.csv into the variable refine.
3. Then set refine to read the 'variable' column and make it into a list using .to_list() and store in name.
4. Create variable var_list and set it to ['NAME'] + name.
5. To create the variable list for the API call by using ','.join() and set to var_string.
6. Create variable api and set it to 'https://api.census.gov/data/2018/acs/acs5' (the url for the American Community Survey 5-Year API endpoint from 2018).
7. Set the for_clause to county:* to return county data.
8. Set in_clause to state:06. The code for California.
9. Use your personal Census API key to set the variable key_value.
10. Create a new dictionary called payload setting keys and values to 'get':var_strong, 'for':for_clause, 'in':in_clause, 'key':key_value.
11. Set response to build a query string using requests.get() with the arguments api and payload.
12. Use a .json() on response to return a list of rows and store in row_list.
13. Set colnames to row_list[0].
14. Set datarows to row_list[1:].
15. Convert data into a pandas dataframe using columns=colnames and data=datarows as the arguments and setting it to ca_data.
16. Orient ca_data using the .set_index() with 'NAME' and inplace=True as the arguments.
17. Out write ca_data to csv called 'census-data-ca.csv.

### Step 2 - Refine and Analyze California Data Collected from the Census
This step is intended to give a better understanding of the California census data and create additional data for further analysis.

1. Create a new python scrip entitled 'analyzed_ca_data.py' and import pandas as pd.
2. To prevent any data supression use pandas to set the  display to max rows using .set_options('display.max_rows, None').
3. Read 'census-data.csv' with the index_col set to 'Variable' into analyze.
4. Set group equal to analyze['Group'] and print group to see the group names.
5. Read 'census-data-ca.csv' with the index set to 'NAME' into health.
6. Apply the .groupby()to health with the arguments group,axis='columns',sort=False to create groub_by.
7. Aggregate the data into by_risk using .sum() on groub_by.
8. Create a list called risk of all strings of variables in 'census-data-ca.csv'.
9. Print by_risk
10. Determine the counties with oldest total median population by setting med_age to by_risk['total median age']. Print  med_age using .sort_values() to determine which counties have the oldest and youngest population, on average. Repeat this step for the median age variable for men ['male'] and women ['female'].
11. Create high_risk_age_male by adding together all age groups from 60 to 85+. Add high_risk_age_male to by_risk by creating a new column ['high risk males']. To determine the percentage of the male population that is at risk store high_risk_age_male divided by by_risk['total'] multipled to 100 to get a percentage. Round to the second decimal place. Store the findings in high_ratio_male and add as a column to by_risk.
12. Repeat step eleven with the female category.
13. Combine high_risk_age_male and high_risk_age_female into high_risk_age. Print high_risk_age to see which counties have the largest high risk population of people over 60. Store high_risk_age as a column in by_risk. Determine the ratio of high risk individuals to the total population by dividing high_risk_age by by_risk[total] multiplied by 100 to create a percentage. Round to the second decimal place and store in hi_ratio. Add hi_ratio to by_risk as a column. Print hi_ratio.
14. Since age is a determinate of risk for corona virus infection it is important to see what California counties have the greatest number of high risk individuals. Create a highest_risk variable for men, women and total, naming them highest_risk_male, highest_risk_female and highest_risk. Store these variables as columns in by_risk. Use the highest_risk variable to determine the percentage of the total population that is at the highest risk, round to two decimal places. Store as additional columns in by_risk. Print the results of the total percentage of the population over 85 using .sort_values().
15. Now store the individual names of counties in county_list and add as a new column to by_risk as ['county']. This ensures a successful join with the COVID-19 data.
16. Finally out write by_risk to 'ca-risk-pop.csv' using to_csv().

### Step 3 - Obtain and Edit COVID-19 Data
In Step 2, the objective is to refine already collected data from the New York Times into a dataset relevant to our analysis here.

1. Download COVID-19 data from the New York Times Github repository (https://github.com/nytimes/covid-19-data)
2. Open a new python script called 'clean-counties.py'
3. Import the pandas module as pd to read the csv us-counties.csv' setting the index column to 'state' using index_col. Store this in the variable county.
4. Drop all non-california observations using the .loc[] command.
5. Further edit the data to remove all but the most recent observations of COVID-19 cases and deaths using the .query with the argument (date ==).
6. Out write county to a csv called 'ca-covid.csv' using the .to_csv function of pandas.

### Step 4- Merge Census Data and COVID-19 Data
Merging the Census Data and COVID-19 Data allows for further analysis.
1. Create a new python script called 'merged.py'.
2. Import the pandas module as pd.
3. Read 'ca-covid.csv' into covid and 'ca-high-risk-pop.csv' into ca using pd.read_csv().
4. Merge the two data sets using covid.merge() with ca and on='county' as the arguments. Store the result in merged.
5. Out write merged to a csv called 'merged.csv' using .to_csv(). This data set will be used for the rest of the analysis.

### Step 5- Create Visualizations
The final step of this project is to create a number of visuals to better understand if there is a relationship between COVID-19 cases and a greater proportion of high risk individuals.
1. Create a new python script 'visualizations.py' and import  pandas as pd, import seaborn as sns and matplotlib.pyplot ans plt.
2. Read 'merged.csv' into the script as covid_risk.
3. Create several simple plots of single variables using sns.distplot of the number of cases, highest risk ratio, deaths and high risk total. Use plt.savefig to save the figures as .pngs.
4. Next plot highest risk by county using sns.barplot and y='highest risk ratio', x='county' and data=covid_risk. Save as a .png.
5. There are a number of more complex visualizations you can create using the covid_risk data.
6. Because some counties are more densely populated and thus  more COVID_19 cases than others like Los Angeles County, create a trimmed down data set that removes high case outliers. Use the .query() with the argument cases fewer than 1000 to create a new data set called outliers.
7. Continue to create visualizations with the trimmed data. In particular using the .regplot function of seaborn to see if there is any relationship between the number of Corona Virus cases in counties with a high proportion of high risk individuals.

## Conclusion
While this analysis does not show a definite link between the number of Corona Virus cases and deaths in California counties with a greater number of individuals in high risk groups, it does offer an interesting look at where extra measures might be considered. It additionally gives us an interesting look at California's demographics. 
