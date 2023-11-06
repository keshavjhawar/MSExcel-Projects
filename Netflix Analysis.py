import pandas as pd
pd.set_option('display.max_columns',20,"display.width",150)

df = pd.read_csv("/Applications/My Projects/Data Analytics/Data Sets/netflix_titles.csv")

# Task 1 : What is the most popular year for movies on netflix?
df['count'] = 1
Release_year = df[df['type']=='Movie'].groupby('release_year').sum().reset_index()[['release_year','count']]
Release_year = Release_year.sort_values(['count'],ascending=False)
# print(Release_year)

# Task 2 : Which year Netflix added most content on its platform?
df['year_added'] = df['date_added'].apply(lambda x: str(x).split(',')[-1])
Added_year = df.groupby('year_added').sum().reset_index()[['year_added','count']]
Added_year = Added_year.sort_values(['count'],ascending=False)
# print(Added_year)

# Task 3 : Independent to year, which is the most popular month to add new content?
df['month_added'] = pd.to_datetime(df['date_added']).dt.month
Added_month = df.groupby('month_added').sum().reset_index()[['month_added','count']]
Added_month = Added_month.sort_values(['count'],ascending=False)
# print(Added_month)

# Task 4 : What is the movie with the longest title in the dataset?
movies = df[df['type'] == 'Movie']
movies['title_size'] = movies['title'].apply(lambda x: len(x))
movies = movies.sort_values('title_size',ascending=False)[['title','title_size']]
# print(movies['title'][5164])

# Task 5 : Which actor/actress shows up most frequently in netflix database?
df_na = df['cast'].dropna()
df_cast = df_na.apply(lambda x: x.split(','))

from collections import Counter
lst = []
for list in df_cast:
    for element in list:
        lst.append(element)

counter = Counter(lst)
most_common = counter.most_common(5)
# print(most_common)
