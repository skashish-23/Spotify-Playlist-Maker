from bs4 import BeautifulSoup
import requests
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy

SPOTIPY_REDIRECT_URI="http://localhost:8888/callback/"

BILLBOARD_HOT_TOP_100 = "https://www.billboard.com/charts/hot-100/"

date = input("Which day do you want the Billboard Top 100 of? Enter YYYY-MM-DD:")
response = requests.get(url=BILLBOARD_HOT_TOP_100+date)
html_page = response.text
soup = BeautifulSoup(html_page, "html.parser")

li_elements = soup.find_all("li")
song_names = []
artist_name = []

for li in li_elements:
    ul_elements = li.find_all("ul")
    for ul in ul_elements:
        inner_li_elements: object = ul.find_all("li")
        for inner_li in inner_li_elements:
            h3_element = inner_li.find("h3", id = "title-of-a-story")
            if h3_element:
                song_names.append(h3_element.text.strip())
                span_element = h3_element.find_next_sibling("span")
                if span_element:
                    artist_name.append(span_element.text.strip())

music_info = list(zip(song_names, artist_name))

#Spotify authentication


SPOTIFY_CLIENT_ID = "5dadeb79d0ee4e1b893cbea2837e3ed8"
UNIQUE_CLIENT_SECRET = "1b8d37e406fc4060916e2633111d6759"

sp= spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = "https://example.com",
        client_id = SPOTIFY_CLIENT_ID,
        client_secret = UNIQUE_CLIENT_SECRET,
        show_dialog = True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
print (user_id)

#search songs on Spotify
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#create a new private playlist
playlist = sp.user_playlist_create(user=user_id, name = f"{date} Billboard 100", public = False)

#adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)