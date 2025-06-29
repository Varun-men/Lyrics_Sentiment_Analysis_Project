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



sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

#1️⃣ Sentiment vs Popularity Correlation
sns.scatterplot(x='Popularity', y='Sentiment Polarity', data=df,palette='coolwarm',size = 'Popularity',hue='Sentiment Polarity',sizes=(50, 300),alpha =0.8)
plt.title('Popularity vs Sentiment Corelation',fontsize=18)
plt.xlabel("Popularity", fontsize=14)
plt.ylabel("Sentiment Polarity", fontsize=14)
plt.legend(title='Sentiment Polarity', bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig("figure-4.1(A).png", dpi=300, bbox_inches='tight')
plt.show()


# Calculate correlation between Popularity and Sentiment Polarity
correlation = df['Popularity'].corr(df['Sentiment Polarity'])
print("Correlation:", correlation)  # Result: -0.0087, no significant relationship


df['Sentiment Category'] = df['Sentiment Polarity'].apply(
    lambda y: 'Positive'if y > 0   else ('Negative' if y < 0   else 'Neutral')
)
# Calculate average popularity per sentiment category
avg_popularity = df.groupby('Sentiment Category')['Popularity'].mean()
print(avg_popularity)  #Result: Positive songs are more popular than negative songs — but the difference is almost negligible (84.27 vs. 83.75).

sns.barplot(x='Sentiment Category', y='Popularity', data=df, estimator='mean', palette='coolwarm')
plt.title("Average Popularity by Sentiment Category")
plt.ylabel("Average Popularity")
plt.grid(True, linestyle='--', linewidth=0.5)
plt.savefig("figure-4.1(B).png", dpi=300, bbox_inches='tight')
plt.show()


#What are the sentiment profiles of the top 5 most popular songs?
top_5_songs = df.sort_values(by='Popularity', ascending=False).head(5)
print(top_5_songs[['Song Title', 'Popularity', 'Sentiment Polarity']])

def categorize_sentiment(score):
    if score>0:
        return 'Positive'
    elif score<0:
        return 'Negative'
    else:
        return 'Neutral'

top_5_songs['Sentiment Category'] = top_5_songs['Sentiment Polarity'].apply(categorize_sentiment)
print(top_5_songs[['Song Title', 'Popularity', 'Sentiment Polarity', 'Sentiment Category']])

# Among the top 5 most popular songs, 4 are categorized as Positive sentiment and 1 as Negative.
# This indicates that while positive sentiment is more common in highly popular songs,
# popularity is not strictly determined by sentiment alone.

sns.set(style='whitegrid')
plt.figure(figsize=(10, 6))
custom_palette = {'Positive': '#2ecc71', 'Negative': '#e74c3c'}
sns.barplot(x='Song Title',y='Popularity',data = top_5_songs,palette=custom_palette,hue='Sentiment Category',  ci=None)
plt.title('Top 5 Most Popular Songs and Their Sentiment Categories',fontsize=16)


for i, row in enumerate(top_5_songs.itertuples()):
    plt.text(i, row.Popularity + 0.5, int(row.Popularity),
             ha='center', va='bottom', fontsize=10, color='black')

plt.xlabel('Song Title',fontsize=16)
plt.ylabel('Popularity',fontsize=13)
plt.xticks(rotation=15, fontsize=11)
plt.yticks(fontsize=11)
plt.legend(title='Sentiment', loc='upper right')
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig("figure-4.1(c).png", dpi=300, bbox_inches='tight')
plt.show()


#Do extreme sentiments affect popularity?
Extreme_Sentiments = df[(df['Sentiment Polarity'] > 0.4) | (df['Sentiment Polarity'] < -0.2)]
print(Extreme_Sentiments[['Song Title', 'Sentiment Polarity','Popularity'] ])

print("Number of extreme sentiment songs:", len(Extreme_Sentiments))
print("Popularity Range (Min to Max):", Extreme_Sentiments['Popularity'].min(), "to", Extreme_Sentiments['Popularity'].max())
print("Average Popularity of extreme sentiment songs:", Extreme_Sentiments['Popularity'].mean())

print("Overall Average popularity:", df['Popularity'].mean())
#Conclusion
#Songs with extreme sentiments (either very positive or negative) tend to be slightly more popular on average (86.33) compared to the overall average (84.2).
#Even with a small sample of 3 songs, the numbers suggest that polarizing songs might attract more attention and popularity.



#How does sentiment polarity differ by popularity tiers?
def categorize_popularity(value):
    if value <= 75:
        return 'Low'
    elif value <= 85:
        return 'Medium'
    else:
        return 'High'
    
df['Popularity Tier'] = df['Popularity'].apply(categorize_popularity)
tier_sentiments = df.groupby('Popularity Tier')['Sentiment Polarity'].mean().reset_index()
print(tier_sentiments)
#Result: since the sentiment polarity for all of these is almost same so sentiment polarity doesnot effect popularity tier!