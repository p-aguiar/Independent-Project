#5 - Create Visualizations 
#%% import modules 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#%% Read Merged Dataset
covid_risk = pd.read_csv('merged.csv')
#%% Create simple plots of single variables
plt.figure()
sns.distplot(covid_risk['cases'])
plt.savefig('simple_cases.png')
plt.figure()
sns.distplot(covid_risk['highest risk ratio'])
plt.savefig('simple_ratio.png')
plt.figure()
sns.distplot(covid_risk['deaths'])
plt.savefig('simple_deaths.png')
plt.figure()
sns.distplot(covid_risk['high risk total'])
plt.savefig('simple_total_risk.png')
#%% Plot highest risk by county
plt.figure()
sns.barplot(y='highest risk ratio',x='county',data=covid_risk)
plt.savefig('risk_county.png')
#%% Plot cases by county
plt.figure()
sns.barplot(y='cases',x='county',data=covid_risk)
plt.savefig('cases_county.png')
#%% Plot deaths by county
plt.figure()
sns.barplot(y='deaths',x='county',data=covid_risk)
plt.savefig('deaths_county.png')
#%% regress total cases and death by total population
plt.figure()
sns.regplot(x="total",y="cases", data=covid_risk)
plt.savefig('reg_cases_total.png')
plt.figure()
sns.regplot(x="total",y="deaths", data=covid_risk)
plt.savefig('reg_deaths_total.png')
#%% regress median age by cases 
plt.figure()
sns.regplot(x="total median age",y="cases", data=covid_risk)
plt.savefig('reg_age_cases.png')
#%% Regress high risk ratio by cases
plt.figure()
sns.regplot(x="highest risk ratio",y="cases", data=covid_risk)
plt.savefig('reg_cases_ratio.png')
#%% Regress high risk ratio by cases organized by county
fg = sns.relplot(x='highest risk ratio',y='cases',col='county', data=covid_risk)
fg.savefig('risk_county.png')
#%% Regress highest risk total by cases
plt.figure()
sns.regplot(x='cases',y='highest risk total', data=covid_risk)
plt.savefig('reg_cases_risk.png')
#%% Create limit plot
plt.figure()
sns.lmplot(x='cases',y='highest risk total', row='county', data=covid_risk)
plt.savefig('reg_cases_risk_county.png')
#%% drop high cases outliers
outlier= covid_risk.query('cases <=1000')
#%% regress high risk ratio by cases using edited data set 
plt.figure()
sns.regplot(x="highest risk ratio",y="cases", data=outlier)
plt.savefig('reg_cases_ratio_edited.png')
#%% joint plot use edited data set 
plt.figure()
multi = sns.jointplot('highest risk ratio','cases', data=outlier,kind='reg')
multi.savefig('joint_edited_risk.png')
#%% regress deaths by high risk population using edited data
plt.figure()
sns.regplot(x="highest risk ratio",y="deaths", data=outlier)
plt.savefig('reg_deaths_ratio_edited.png')
#%% regress median age by cases and death using edited data
plt.figure()
sns.regplot(x="total median age",y="cases", data=outlier)
plt.savefig('reg_age_cases_edited.png')
plt.figure()
sns.regplot(x="total median age",y="deaths", data=outlier)
plt.savefig('reg_age_cases_edited.png')
