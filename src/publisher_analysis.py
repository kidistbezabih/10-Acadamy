import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load dataset
df = pd.read_csv('data/dataset.csv')

# 1. Publisher Contribution Analysis
publisher_counts = df['publisher'].value_counts()

# Top 10 publishers
top_publishers = publisher_counts.head(10)

# Plot Top Publishers
plt.figure(figsize=(10, 6))
top_publishers.plot(kind='bar', color='skyblue', title='Top 10 Publishers')
plt.xlabel('Publisher')
plt.ylabel('Number of Articles')
plt.grid()
plt.show()

# Save top publishers to a CSV
top_publishers.to_csv('data/top_publishers.csv', header=['Article Count'])

# 2. Extract Unique Domains
def extract_domain(publisher):
    if '@' in publisher:
        return publisher.split('@')[-1]
    return None

df['domain'] = df['publisher'].apply(lambda x: extract_domain(str(x)))

# Count contributions by domain
domain_counts = df['domain'].value_counts().dropna()

# Top 10 domains
top_domains = domain_counts.head(10)

# Plot Top Domains
plt.figure(figsize=(10, 6))
top_domains.plot(kind='bar', color='orange', title='Top 10 Domains')
plt.xlabel('Domain')
plt.ylabel('Number of Articles')
plt.grid()
plt.show()

# Save top domains to a CSV
top_domains.to_csv('data/top_domains.csv', header=['Article Count'])

# 3. Reporting Differences (Sentiment Analysis Example)
# Example: Group by publisher and analyze sentiment (if sentiment column exists)
if 'sentiment' in df.columns:
    sentiment_by_publisher = df.groupby('publisher')['sentiment'].value_counts().unstack().fillna(0)

    # Save sentiment breakdown by publisher
    sentiment_by_publisher.to_csv('data/sentiment_by_publisher.csv')

print("Publisher analysis completed. Results saved in 'data/'.")
