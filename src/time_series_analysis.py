import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/dataset.csv')

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Remove rows with invalid dates
df = df.dropna(subset=['date'])

# Extract components for analysis
df['day'] = df['date'].dt.date
df['hour'] = df['date'].dt.hour
df['weekday'] = df['date'].dt.day_name()

# 1. Daily Publication Frequency
daily_counts = df.groupby('day').size()

# Plot daily trends
plt.figure(figsize=(12, 6))
daily_counts.plot(kind='line', title='Daily Publication Frequency', color='blue')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.grid()
plt.show()

# 2. Hourly Distribution
hourly_counts = df.groupby('hour').size()

# Plot hourly trends
plt.figure(figsize=(10, 5))
hourly_counts.plot(kind='bar', color='orange', title='Hourly Distribution of Publications')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Articles')
plt.grid()
plt.show()

# 3. Weekday Distribution
weekday_counts = df.groupby('weekday').size()

# Plot weekday trends
plt.figure(figsize=(8, 4))
weekday_counts.plot(kind='bar', color='green', title='Articles Published by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Articles')
plt.grid()
plt.show()

# Save the results
daily_counts.to_csv('data/daily_counts.csv', header=['Publication Count'])
hourly_counts.to_csv('data/hourly_counts.csv', header=['Publication Count'])
weekday_counts.to_csv('data/weekday_counts.csv', header=['Publication Count'])

print("Time Series Analysis completed. Results saved in 'data/'.")
