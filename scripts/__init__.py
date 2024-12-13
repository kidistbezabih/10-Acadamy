import pandas as pd

df = pd.read_csv('data/raw_analyst_ratings.csv');

# Add a column for headline length
df['headline_length'] = df['headline'].apply(len)

# Basic statistics for headline lengths
headline_stats = df['headline_length'].describe()
print("Headline Length Statistics:\n", headline_stats)

# Count the number of articles per publisher
publisher_counts = df['publisher'].value_counts()
print("Articles per Publisher:\n", publisher_counts)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract publication day, month, or week
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Group by date to analyze trends
daily_counts = df.groupby(df['date'].dt.date).size()
print("Daily Article Counts:\n", daily_counts)


import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of headline lengths
plt.figure(figsize=(8, 5))
sns.histplot(df['headline_length'], bins=30, kde=True)
plt.title("Distribution of Headline Lengths")
plt.xlabel("Headline Length")
plt.ylabel("Frequency")
plt.show()

# Bar chart for top publishers
top_publishers = publisher_counts.head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_publishers.index, y=top_publishers.values)
plt.title("Top 10 Publishers by Article Count")
plt.xlabel("Publisher")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45)
plt.show()

# Line chart for daily article counts
plt.figure(figsize=(12, 5))
daily_counts.plot(kind='line')
plt.title("Daily Article Publication Trend")
plt.xlabel("Date")
plt.ylabel("Number of Articles")
plt.grid()
plt.show()
