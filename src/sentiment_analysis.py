import pandas as pd
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load the dataset
df = pd.read_csv('data/dataset.csv')

# Clean and preprocess headlines
def clean_text(text):
    return ' '.join(word for word in text.lower().split() if word not in stop_words)

df['cleaned_headline'] = df['headline'].apply(clean_text)

# Perform Sentiment Analysis
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

df['sentiment'] = df['cleaned_headline'].apply(get_sentiment)

# Save results
df[['headline', 'sentiment']].to_csv('data/sentiment_results.csv', index=False)
print("Sentiment Analysis completed. Results saved to 'data/sentiment_results.csv'")
