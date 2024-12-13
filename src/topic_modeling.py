import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from gensim import corpora, models

# Load data
df = pd.read_csv('data/dataset.csv')

# Tokenize headlines
df['tokens'] = df['cleaned_headline'].apply(word_tokenize)

# Keyword Extraction
vectorizer = CountVectorizer(max_features=20, stop_words='english')
keywords = vectorizer.fit_transform(df['cleaned_headline'])
print("Top Keywords:", vectorizer.get_feature_names_out())

# Topic Modeling with Gensim
# Prepare data for LDA
dictionary = corpora.Dictionary(df['tokens'])
corpus = [dictionary.doc2bow(tokens) for tokens in df['tokens']]

# Apply LDA
lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10)

# Print Topics
print("LDA Topics:")
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx}: {topic}")

# Save results
lda_model.save('models/topic_model.lda')
print("Topic Modeling completed. Model saved to 'models/topic_model.lda'")
