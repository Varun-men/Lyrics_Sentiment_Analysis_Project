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

#3️⃣ Popularity Trend Over Time
#Are newer songs more popular or older classics?
df.loc[df['Release Date'] == '2015', 'Release Date'] = '2015-01-01'
df['release_date'] = pd.to_datetime(df['Release Date'])
df['Release Year'] = df['release_date'].dt.year
Popularity= df.groupby('Release Year')['Popularity'].mean()
print(Popularity)

plt.plot(Popularity.index,Popularity.values,color='red',marker ='o',label='Popularity Over Year')
plt.title("Average Popularity by Release Year", fontsize=16, weight='bold')
plt.xlabel('Release Year', fontsize=12)
plt.ylabel("Average Popularity", fontsize=12)
plt.xticks(Popularity.index)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend()
plt.gca().set_facecolor('whitesmoke')
plt.tight_layout()
plt.savefig("figure-4.3(a).png", dpi=300, bbox_inches='tight')
plt.show()
#Result: newer songs tend to be more popular than older classics


#Is the popularity of songs increasing or decreasing over the years?
#Result: Yes — newer songs (till 2022) are generally more popular than
# older classics, but the popularity is not increasing consistently year after year


#3-year Moving Average Line (Priority: Medium-High)
moving_avg = Popularity.rolling(window=3).mean()
plt.figure(figsize=(10,6))
Popularity.plot(kind='line', marker='o', color='red', label='Actual Popularity')
moving_avg.plot(kind='line', marker='o', color='blue', label='3-Year Moving Average')
plt.title('Average Popularity by Release Year with 3-Year Moving Average',fontsize=16, weight='bold')
plt.xlabel('Release Year',fontsize=16)
plt.ylabel('Average Popularity',fontsize=16)
plt.xticks(Popularity.index)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend()
plt.gca().set_facecolor('whitesmoke')
plt.tight_layout()
plt.savefig("figure-4.3(b).png", dpi=300, bbox_inches='tight')
plt.show()

#Which year(s) had the highest and lowest average popularity?
highest_popularity = Popularity.values.max()
lowest_popularity = Popularity.values.min()

highest_year = Popularity[Popularity == highest_popularity].index.tolist()
lowest_year = Popularity[Popularity == lowest_popularity].index.tolist()

print("Highest Average Popularity was in the year :",highest_year,"\nLowest Average Popularity was in the year :",lowest_year)


#Grouped Popularity Analysis
df['5_Year_Group'] = (df['Release Year'] // 5) * 5
five_year_avg = df.groupby('5_Year_Group')['Popularity'].mean()
plt.figure(figsize=(8,5))
five_year_avg.plot(kind='bar', color='orange')
plt.title('Average Popularity by 5-Year Interval', fontsize=16, weight='bold')
plt.xlabel('5-Year Interval', fontsize=16)
plt.ylabel('Average Popularity', fontsize=16)
plt.xticks(rotation=0)
plt.grid(True, linestyle='--', alpha=0.4)
plt.gca().set_facecolor('whitesmoke')
plt.tight_layout()
plt.savefig("figure-4.3(c).png", dpi=300, bbox_inches='tight')
plt.show()

# Result:
# The 5-Year Average Popularity bar chart shows that the interval with the highest 
# average popularity was [insert highest 5-year group here] (e.g. 2020–2024), 
# while the lowest was in [insert lowest 5-year group here]. 
# This indicates that recent years generally have higher popularity averages, 
# though there are noticeable fluctuations between periods.