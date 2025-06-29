import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("final_song_dataset_with_sentiment.csv")
print(df)

df.head()
df.columns
df.info()
#checking if there is any null value in the dataset
print(df.isnull().sum())

#if any null value found in any column then droping the row where its null
df.dropna(inplace=True)


##Grouped Popularity Analysis
top_10_artists = df['Artist'].value_counts().head(10)
print(top_10_artists)

plt.figure(figsize=(10,5))
sns.barplot(x=top_10_artists.index, y=top_10_artists.values, palette='viridis')
plt.title('Top 10 Artists with Most Songs', fontsize=16, weight='bold')
plt.xlabel('Artist', fontsize=12)
plt.ylabel('Number of Songs', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("figure-4.4(a).png", dpi=300, bbox_inches='tight')
plt.show()
#Result: Artist
# Ed Sheeran        5
# Maroon 5          2
# Lil Nas X         2
# The Weeknd        1
# Adele             1
# Wiz Khalifa       1
# Alec Benjamin     1
# Dua Lipa          1
# Camila Cabello    1
# Mark Ronson       1


#4️⃣ Which Artists Have the Most Positive/Negative Songs
Average_Sentiment = df.groupby('Artist')['Sentiment Polarity'].mean().reset_index()
print(Average_Sentiment)
sns.set(style="whitegrid")
plt.figure(figsize=(12,6))
sns.barplot(x='Artist',y='Sentiment Polarity',data =Average_Sentiment,estimator='mean', palette='coolwarm')
plt.title("Average Sentiment by Artist", fontsize=18, weight='bold',color='#333333')
plt.xlabel('Artists Name', fontsize=14)
plt.ylabel("Average Sentiment", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45, ha='right', fontsize=12)
for index, row in Average_Sentiment.iterrows():
    plt.text(index, row['Sentiment Polarity'] + 0.01, f"{row['Sentiment Polarity']:.2f}", ha='center', fontsize=10)
plt.gca().set_facecolor('whitesmoke')
plt.tight_layout()
plt.savefig("figure-4.4(b).png", dpi=300, bbox_inches='tight')
plt.show()

positive_counts = df[df['Sentiment Polarity'] > 0]['Artist'].value_counts()
negative_counts = df[df['Sentiment Polarity'] < 0]['Artist'].value_counts()

print("Artist with most positive songs:", positive_counts.idxmax(), "with", positive_counts.max(), "songs")
print("Artist with most negative songs:", negative_counts.idxmax(), "with", negative_counts.max(), "songs")

#Result: Artist with most positive songs: Dua Lipa with 7 songs
#Artist with most negative songs: Billie Eilish with 6 songs


#Distribution of Sentiment Scores for Top 5 Artists (Violin/Box Plot)
top_5_artists = df['Artist'].value_counts().head(5).index.tolist()
top_5_df = df[df['Artist'].isin(top_5_artists)]
plt.figure(figsize=(10,6))
sns.boxplot(x='Artist', y='Sentiment Polarity', data=top_5_df,palette='viridis')
plt.title("Distribution of Sentiment Scores for Top 5 Artists", fontsize=18, weight='bold', color="#000000")
plt.xlabel('Artist', fontsize=14)
plt.ylabel('Sentiment Polarity', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.gca().set_facecolor('whitesmoke')
plt.tight_layout()
plt.savefig("figure-4.4(c).png", dpi=300, bbox_inches='tight')
plt.show()

#Ed Sheeran appears to consistently produce emotionally positive songs with a noticeable range, 
# while other artists either have fewer songs or their sentiment polarity clusters within narrower, mostly positive ranges.


# Artist-wise Positive vs Negative Song Count
df['Sentiment Label'] = df['Sentiment Polarity'].apply(lambda x: 'Positive' if x > 0 else 'Negative')
artist_sentiment_count = df.groupby(['Artist', 'Sentiment Label']).size().reset_index(name='Count')
print(artist_sentiment_count.head())
plt.figure(figsize=(12,6))
sns.barplot(x='Artist', y='Count', hue='Sentiment Label', data=artist_sentiment_count, palette='viridis')
plt.title('Artist-wise Positive vs Negative Song Count', fontsize=18, weight='bold')
plt.xlabel('Artist', fontsize=14)
plt.ylabel('Number of Songs', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.gca().set_facecolor('whitesmoke')
plt.tight_layout()
plt.savefig("figure-4.4(d).png", dpi=300, bbox_inches='tight')
plt.show()
#Conclusion: 