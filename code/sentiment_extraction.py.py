import pandas as pd
from textblob import TextBlob

df = pd.read_csv("raw_songs_dataset.csv")

def get_sentiment(text):
    try:
        analysis = TextBlob(str(text))
        return analysis.sentiment.polarity
    except:
        return 0

df['Sentiment Polarity'] = df['Lyrics'].apply(get_sentiment)

df.to_csv("final_song_dataset_with_sentiment.csv", index=False, encoding='utf-8-sig')

print("✅ Sentiment analysis added and saved to final_song_dataset_with_sentiment.csv")