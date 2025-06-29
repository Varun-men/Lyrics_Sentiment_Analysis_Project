import requests
import base64
from bs4 import BeautifulSoup
import pandas as pd
import time

client_id = 'cd7834d216434ea38eca7100f6baade5'
client_secret = '005ee4379b7545ffba187458629ec213'

genius_token = 'Bearer ShCw439vtL8FMzDFlHqmArpIcpqNHs9wYXhj2YEkY1C1QdI0DXGrDjzZig_d0Ki_'

def get_spotify_token(client_id, client_secret):
    token_url = 'https://accounts.spotify.com/api/token'
    credentials = f"{client_id}:{client_secret}"
    credentials_b64 = base64.b64encode(credentials.encode()).decode()

    headers = {'Authorization': f'Basic {credentials_b64}'}
    data = {'grant_type': 'client_credentials'}

    response = requests.post(token_url, headers=headers, data=data)
    return response.json()['access_token']

spotify_token = get_spotify_token(client_id, client_secret)


def get_spotify_data(song_title, token):
    search_url = "https://api.spotify.com/v1/search"
    headers = {'Authorization': f'Bearer {token}'}
    params = {'q': song_title, 'type': 'track', 'limit': 1}

    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()

    try:
        track = data['tracks']['items'][0]
        popularity = track['popularity']
        release_date = track['album']['release_date']
        artist_name = track['artists'][0]['name']
        return artist_name, popularity, release_date
    except IndexError:
        return "Not Found", "N/A", "N/A"



def get_lyrics_url(song_title, genius_token):
    base_url = 'https://api.genius.com/search'
    headers = {'Authorization': genius_token}
    params = {'q': song_title}

    response = requests.get(base_url, headers=headers, params=params)
    data = response.json()

    try:
        url = data['response']['hits'][0]['result']['url']
        return url
    except IndexError:
        return "N/A"

def scrape_lyrics(url):
    if url == "N/A":
        return "Lyrics not found"
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        lyrics_containers = soup.find_all('div', attrs={"data-lyrics-container": "true"})
        lyrics = "\n".join([div.get_text(separator="\n") for div in lyrics_containers])
        return lyrics
    except:
        return "Lyrics scrape failed"

songs = [
    "Blinding Lights", "Shape of You", "Let Me Down Slowly", "Levitating",
    "Someone Like You", "See You Again", "Uptown Funk", "Havana",
    "Despacito", "Senorita", "Believer", "Counting Stars", "Perfect",
    "Memories", "Stay", "Love Me Like You Do", "Photograph", "Girls Like You",
    "Peaches", "Shivers", "Thinking Out Loud", "Faded", "Stitches",
    "Bad Guy", "Attention", "Old Town Road", "Drivers License",
    "Industry Baby", "As It Was", "Daylight"
]

results = []

for song in songs:
    print(f"Fetching data for: {song}")

    artist, popularity, release_date = get_spotify_data(song, spotify_token)

    lyrics_url = get_lyrics_url(song, genius_token)
    lyrics = scrape_lyrics(lyrics_url)

    results.append({
        'Song Title': song,
        'Artist': artist,
        'Popularity': popularity,
        'Release Date': release_date,
        'Lyrics URL': lyrics_url,
        'Lyrics': lyrics
    })

    time.sleep(2)  

df = pd.DataFrame(results)
df.to_csv("raw_song_dataset.csv", index=False, encoding='utf-8-sig', quoting=1)


print("✅ All song data saved successfully to raw_songs_dataset.csv")