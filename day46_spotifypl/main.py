import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from top100 import top100

load_dotenv()

'''SPOTIFY GLOBALS'''
SPOTIFY_CLIENT_ID = os.getenv("ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SECRET")
REDIRECT_URI = 'https://example.org/callback'

scope = "playlist-modify-private"

'''set up spotify client'''
sp_oauth = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=REDIRECT_URI,
                        scope=scope, cache_path='./.cache')
sp = spotipy.Spotify(auth_manager=sp_oauth)

USER = sp.current_user()
# a dictionary: {'display_name': 'Zander Alt',
# 'external_urls': {'spotify': 'https://open.spotify.com/user/31o4birrgequtgkrzpoffgtcabru'},
# 'href': 'https://api.spotify.com/v1/users/31o4birrgequtgkrzpoffgtcabru', 'id': '31o4birrgequtgkrzpoffgtcabru',
# 'images': [], 'type': 'user', 'uri': 'spotify:user:31o4birrgequtgkrzpoffgtcabru',
# 'followers': {'href': None, 'total': 0}}

'''get top 100 songs'''
date = input("What year your would you like to travel to? (YYYY-MM-DD): ")
year = date[0:4]
songs = top100(date)

song_uris = []
to_remove = []
for song in songs:
    try:
        uri = sp.search(q=f"track:{song.getText().strip()}, year:1900-{year}", type='track')["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} is not available on spotify, skipping...")
        to_remove.append(song)

for song in to_remove:
    songs.remove(song)

new_playlist = sp.user_playlist_create(user=USER["id"], name=f"{date} TOP 100 BILLBOARD", public=False)
sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)







# url = f"https://www.billboard.com/charts/hot-100/{date}/"
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
#
# songs = [song.find(name="h3") for song in soup.find_all(name="li", class_="o-chart-results-list__item") if song.find(name="h3")]
#
# for song in songs:
#     print(song.getText().strip())
#
# print(len(songs))