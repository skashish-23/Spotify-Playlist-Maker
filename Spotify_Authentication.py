import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

os.environ["SPOTIFY_CLIENT_ID"] = ""
os.environ["UNIQUE_CLIENT_SECRET"] = ""

sp= spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = "https://example.com",
        client_id = "SPOTIFY_CLIENT_ID",
        client_secret = "UNIQUE_CLIENT_SECRET",
        show_dialog = True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#search songs on Spotify
song_uris = []
year = date.split("-")[0]
