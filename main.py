import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('netflix_titles.csv')


num_TV_shows = df[df['type'] == 'TV Show'].shape[0]
print("Number of TV Shows:", num_TV_shows)


num_movies = df[df['type'] == 'Movie'].shape[0]
print("Number of Movies:", num_movies)


# pie chart to show the distribution of tv shows vs movies in the dataset
movies_vs_tv = plt.pie([num_TV_shows, num_movies], labels=[
                       'TV Shows', 'Movies'], autopct='%1.1f%%')
plt.title('Distribution of TV Shows and Movies on Netflix')
plt.show()


# The most common rating in the dataset
most_common_rating = df['rating'].mode()[0]
print("Most common rating:", most_common_rating)


# selects the column of release year and then counts the number of movies released each yr
# idxmax give the year with maximum count of movies
# max() will give us the maximum number of movies released in a yr
most_common_release_year = df['release_year'].value_counts().idxmax()
most_releases = df['release_year'].value_counts().max()
print("Most common release year:", most_common_release_year)
print("Number of releases in most common year:", most_releases)


# bar graph to depict movies and tv shows releassed each year
release_year_counts = df['release_year'].value_counts().sort_index()
plt.bar(release_year_counts.index, release_year_counts.values)
plt.xlabel('Release Year')
plt.ylabel('Number of Movies and TV Shows')
plt.title('Number of Movies and TV Shows Released Each Year')
plt.show()

# most listed in aka genre which is most common in the dataset
most_listed_in = df['listed_in'].value_counts().idxmax()
print("Most common listed in:", most_listed_in)


# second most listed in aka genre which is most common in the dataset
most_common_listed_in = df['listed_in'].value_counts().head(5)
print("Most common listed in:", most_common_listed_in)

# The most common country of origin for the movies and TV shows in the dataset
most_common_country = df['country'].dropna().value_counts().idxmax()
print("Most common country of origin:", most_common_country)


# top directors
top_directors = df['director'].value_counts().head(5)
print("Top Directors:", top_directors)


# Movies vs TV Shows by Year
line_graph = pd.crosstab(df['release_year'], df['type'])
line_graph.plot(kind='line')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.title('Movies vs TV Shows by Year')
plt.show()


# Oldest Content on Netflix
oldest_content = df.loc[df['release_year'].idxmin()]
print("Oldest content on Netflix:")
print(oldest_content[['title', 'release_year']])


# average duration of movies
# we will first filter the movies and then extract the duration column and then calculate the mean
average_movie_duration = df[df['type'] == 'Movie']['duration'].str.extract(
    '(\d+)').astype(float).mean()[0]
print("Average duration of movies:", average_movie_duration, "minutes")


# Top 10 Actors
top_actors = (
    df['cast']
    .dropna()
    .str.split(', ')
    .explode()
    .value_counts()
    .head(10)
)

print("Top 10 Actors:", top_actors)

# dropping the description column as not required
drop_column = df.drop(columns=['description', 'date_added'])


# saving the cleaned dataset to a new csv file
drop_column.to_csv('cleaned_netflix_titles.csv', index=False)
