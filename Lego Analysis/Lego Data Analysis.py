import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
pd.set_option('display.max_columns',10)

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/lego_sets.csv')
parent_theme = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/parent_themes.csv')

# Task1 : What percentage of all licensed sets ever released were Star Wars themed? Save
# your answer as a variable the force in the form of an integer (e.g. 25).

merged = df.merge(parent_theme,right_on = 'name',left_on = 'theme_name')
merged = merged.drop(columns = 'name_y')
licensed = merged[merged['is_licensed']]
licensed = licensed.dropna(subset = ['set_num'])
starwar = licensed[licensed['parent_theme'] == 'Star Wars']
# print(starwar)
force = int((starwar.shape[0]/licensed.shape[0])*100)
# print(force)

# Task2 : In which year was Star Wars not the most popular licensed theme (in terms of
# number of sets released that year)? Save your answer as a variable new_era in the
# form of an integer (e.g. 2012).
# print(starwar.groupby('year').count())
print(licensed.groupby(['year','parent_theme']).count())
