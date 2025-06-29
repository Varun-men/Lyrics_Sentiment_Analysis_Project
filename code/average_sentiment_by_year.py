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


#2️⃣ Average Sentiment by Release Year
df.loc[df['Release Date'] == '2015', 'Release Date'] = '2015-01-01'
df['release_date'] = pd.to_datetime(df['Release Date'])
df['Release Year'] = df['release_date'].dt.year
Average_Sentiment = df.groupby('Release Year')['Sentiment Polarity'].mean()
print(Average_Sentiment)

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x='Release Year', y='Sentiment Polarity', data=df, estimator='mean', palette='coolwarm')
plt.title("Average Sentiment by Release Year", fontsize=16, weight='bold')
plt.xlabel('Release Year', fontsize=12)
plt.ylabel("Average Sentiment", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.4)
plt.gca().set_facecolor('whitesmoke')
plt.tight_layout()
plt.savefig("figure-4.2(a).png", dpi=300, bbox_inches='tight')
plt.show()


#Are songs becoming sadder, happier, or more neutral over time?
plt.plot(Average_Sentiment.index, Average_Sentiment.values ,color='red',marker ='o',label='Sentiment each year')
plt.title("Average Sentiment by Release Year", fontsize=16, weight='bold')
plt.xlabel('Release Year', fontsize=12)
plt.ylabel("Average Sentiment", fontsize=12)
plt.xticks(Average_Sentiment.index)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend()
plt.gca().set_facecolor('whitesmoke')
plt.tight_layout()
plt.savefig("figure-4.2(b).png", dpi=300, bbox_inches='tight')
plt.show()
#Result: While average sentiment in songs peaked in 2020,
# recent years show a noticeable decline towards neutrality, suggesting a trend of more emotionally balanced or neutral songs in the industry.


#Which year had the highest and lowest average sentiment?
highest_sentiment = Average_Sentiment.values.max()
lowest_sentiment = Average_Sentiment.values.min()

highest_year = Average_Sentiment[Average_Sentiment == highest_sentiment].index.tolist()
lowest_year = Average_Sentiment[Average_Sentiment == lowest_sentiment].index.tolist()

print("Highest Average sentiment was in the year :",highest_year,"\nLowest Average Sentiment was in the year :",lowest_year)
#Result:
#Highest Average sentiment was in the year : [2020] 
#Lowest Average Sentiment was in the year : [2013]


#Has the sentiment trend been stable or volatile over the years?
yearly_changes = Average_Sentiment.diff().abs()
average_change = yearly_changes.mean()

print(yearly_changes)
print("Average year-on-year change in sentiment:", round(average_change, 3))
#average change is relatively high >0.1 which suggests volatility.


#Is there a noticeable difference between recent years (last 5 years) and earlier years?
earlier_years_avg = Average_Sentiment[Average_Sentiment.index < 2019].mean()
recent_years_avg = Average_Sentiment[Average_Sentiment.index >= 2019].mean()

print("Average sentiment before 2019:", round(earlier_years_avg, 3))
print("Average sentiment from 2019 onwards:", round(recent_years_avg, 3))
labels = ['Before 2019', '2019 onwards']
averages = [round(earlier_years_avg, 3), round(recent_years_avg, 3)]
plt.figure(figsize=(6,4))
plt.bar(labels, averages, color=['skyblue', 'salmon'])

for i, v in enumerate(averages):
    plt.text(i, v + 0.005, f"{v:.3f}", ha='center', fontsize=11)

plt.title('Average Sentiment: Before vs After 2019', fontsize=14, weight='bold')
plt.ylabel('Average Sentiment Polarity')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.gca().set_facecolor('whitesmoke')
plt.tight_layout()
plt.savefig("figure-4.2(c).png", dpi=300, bbox_inches='tight')
plt.show()
#Result: Songs from 2019 onwards are, on average, less positive in sentiment compared to those released before 2019.