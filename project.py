import numpy as np
import pandas as pd

k=pd.read_csv('Covid Analysis - Phase 1.csv')


num_countries = k['Country/Region'].nunique()

null_values = k.isnull()

print(null_values)

k.isnull().sum()

print("the total no of null values are:",k)

max_cases=k[k['Confirmed'] ==k['Confirmed'].max() ]

print("country wtih max cases are:",max_cases[['Country/Region'] ])

max_death= k[k['Deaths'] ==k['Deaths'].max() ]

print("country with heighest deaths is :",max_death['Country/Region'])

print("mean is",k['Confirmed'].mean())

total_deaths= k['Deaths'].sum()
print("total no of deaths are:",total_deaths)

total_cases=k['Deaths'].sum()

print("total no of covid cases are:",total_cases)

k.insert(1,"pdeath" ,(k['Deaths']/k['Confirmed'])*100)

maxpercentaged = k[k['pdeath'] ==k['pdeath'].max()]

print("country with max death percentage is:",maxpercentaged['Country/Region'])

k.insert(1,"r",(100-(k['Deaths']/k['Confirmed'])*100))

rec = k[k['r']==k['r'].max()]

print(rec['Country/Region'])

k.insert(1,"newCasesToActiveCases",(k['New cases']/k['Active']))

print(k)

df = pd.DataFrame(k)

filtered_df =df[df['WHO Region']=='Africa']

print(filtered_df)


