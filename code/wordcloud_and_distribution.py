import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv("final_song_dataset_with_sentiment.csv")


# 5️⃣ Word Clouds
# A Word Cloud (or tag cloud) is a visual representation of text data, where:
# Words from the text appear in different sizes.
# The size of each word represents its frequency or importance in the text.
# Words that appear more frequently in the text are displayed larger and bolder.

positive_lyrics = df[df['Sentiment Polarity'] > 0.2]['Lyrics'].str.cat(sep=' ')
negative_lyrics = df[df['Sentiment Polarity'] < -0.2]['Lyrics'].str.cat(sep=' ')
wordcloud_positive = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(positive_lyrics)
wordcloud_negative = WordCloud(width=800, height=400, background_color='black', colormap='Reds').generate(negative_lyrics)
plt.figure(figsize=(20, 10))
plt.subplot(1, 2, 1)
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.title('Positive Songs Word Cloud', fontsize=20)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.title('Negative Songs Word Cloud', fontsize=20)
plt.axis('off')

plt.tight_layout(pad=3)
plt.savefig("figure-4.5(a).png", dpi=300, bbox_inches='tight')
plt.show()


# Top 10 Most Common Words in Positive vs Negative Songs
positive_words_series = pd.Series(positive_lyrics.split())
negative_words_series = pd.Series(negative_lyrics.split())
top_10_positive =  positive_words_series.value_counts().head(10)
top_10_negative =  negative_words_series.value_counts().head(10)
print("Top 10 Positive Words:\n", top_10_positive)
print("\nTop 10 Negative Words:\n", top_10_negative)

sns.barplot(x=top_10_positive.index, y=top_10_positive.values, palette='viridis')
plt.title('Top 10 Common Words in Positive Songs', fontsize=16, weight='bold')
plt.xlabel('Words', fontsize=12)
plt.ylabel('Number of Occurence', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("figure-4.5(b).png", dpi=300, bbox_inches='tight')
plt.show()

sns.barplot(x=top_10_negative.index, y=top_10_negative.values, palette='viridis')
plt.title('Top 10 Common Words in Negative Songs', fontsize=16, weight='bold')
plt.xlabel('Words', fontsize=12)
plt.ylabel('Number of Occurence', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("figure-4.5(c).png", dpi=300, bbox_inches='tight')
plt.show()

# Top 10 Positive Words:
#  you     158
# I       118
# the      97
# me       83
# my       75
# in       69
# (        60
# )        59
# I'm      56
# like     53
# Name: count, dtype: int64

# Top 10 Negative Words:
#  guy       15
# I'm       13
# bad       12
# your       9
# I          8
# the        8
# a          7
# you        7
# type       6
# you're     5



#Average Word Count in Positive vs Negative Songs
df['Word_Count'] = df['Lyrics'].apply(lambda x: len(str(x).split()))
avg_word_count_positive = df[df['Sentiment Polarity'] > 0.2]['Word_Count'].mean()
avg_word_count_negative = df[df['Sentiment Polarity'] < -0.2]['Word_Count'].mean()
print("Average Word Count in Positive Songs:", avg_word_count_positive)
print("Average Word Count in Negative Songs:", avg_word_count_negative)

avg_counts = pd.Series({'Positive Songs': avg_word_count_positive,'Negative Songs': avg_word_count_negative})

sns.barplot(x=avg_counts.index, y=avg_counts.values, palette=['lime','red'])
plt.title('Average Word Count: Positive vs Negative Songs', fontsize=16, weight='bold')
plt.ylabel('Average Number of Words', fontsize=12)
plt.xlabel('Song Sentiment', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("figure-4.5(d).png", dpi=300, bbox_inches='tight')
plt.show()
## Conclusion:
# Positive songs have a higher average word count (535.88) than negative songs (337.00).
# This indicates that happy or upbeat songs tend to be longer and more descriptive,
# while negative songs are generally shorter and more concise.


#Most Positive and Most Negative Song
most_positive_song = df.loc[df['Sentiment Polarity'].idxmax()]
most_negative_song = df.loc[df['Sentiment Polarity'].idxmin()]
print("🎶 Most Positive Song:")
print("Title:", most_positive_song['Song Title'])
print("Artist:", most_positive_song['Artist'])
print("Polarity Score:", most_positive_song['Sentiment Polarity'])
print("Lyrics Snippet:", most_positive_song['Lyrics'][:300], "...\n")

print("🎶 Most Negative Song:")
print("Title:", most_negative_song['Song Title'])
print("Artist:", most_negative_song['Artist'])
print("Polarity Score:", most_negative_song['Sentiment Polarity'])
print("Lyrics Snippet:", most_negative_song['Lyrics'][:300], "...")

extreme_polarity = pd.Series({'Levitating (Dua Lipa)': 0.545770202020202,'Bad Guy (Billie Eilish)': -0.2962261904761904})
sns.barplot(x=extreme_polarity.index,y=extreme_polarity.values, palette=["#F621B2", "#68097D"])
plt.title('Most Positive vs Most Negative Song Polarity', fontsize=14, weight='bold')
plt.ylabel('Polarity Score')
plt.xlabel("Artist")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("figure-4.5(e).png", dpi=300, bbox_inches='tight')
plt.show()
#Most Positive Song:
# Title: Levitating
# Artist: Dua Lipa
# Polarity Score: 0.545770202020202
# Lyrics Snippet: 166 Contributors

#Most Negative Song:
# Title: Bad Guy
# Artist: Billie Eilish
# Polarity Score: -0.2962261904761904
# Lyrics Snippet: 360 Contributors


#Sentiment Distribution Plot
sns.histplot(df['Sentiment Polarity'], bins=30, kde=True, color='#26A69A')
plt.title('Sentiment Polarity Distribution', fontsize=16, weight='bold')
plt.xlabel('Sentiment Polarity Score')
plt.ylabel('Number of Songs')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("figure-4.5(f).png", dpi=300, bbox_inches='tight')
plt.show()
#Conclusion:
# The sentiment polarity distribution shows that most songs in the 
# dataset are clustered around neutral to mildly positive sentiment. 
# There are very few songs with strong negative sentiment, indicating 
# a dataset that slightly leans towards optimistic and upbeat lyrical content.



#=====================================THE END===================================