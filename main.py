import requests
import json
from secrets import user_id, user_token

class Youtube2Spotify:
	def __init__(self):
		self.user_id = user_id
		self.user_token = user_token
		self.headers = {
			'Content-Type' : 'application/json',
			'Authorization' : f'Bearer {self.user_token}'
			}

	def create_spotify_playlist(self, pl_name, pl_desc, public):
		url = f'https://api.spotify.com/v1/users/{self.user_id}/playlists'

		data = json.dumps({
			'name' : pl_name,
			'description' : pl_desc,
			'public' : public
		})

		response = requests.post(url, data=data, headers=self.headers)

		if response.status_code == 201:
			print("Created playlist successfully!")

			return response.json()['id']

	def search_spotify(self, query):
		url = 'https://api.spotify.com/v1/search'

		data = {
			'q' : query,
			'type' : 'track'
			}

		response = requests.get(url, params=data, headers=self.headers)

		if response.status_code == 200:
			songs = response.json()['tracks']['items']
			if len(songs):
				first_song_uri = songs[0]['uri']

				return first_song_uri

	def add_to_spotify(self, playlist_id, song_uris):
		url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
		
		data = json.dumps({
			'uris' : song_uris,
			})	

		response = requests.post(url, data=data, headers=self.headers)

		if response.status_code == 201:
			print("Songs added successfully!")
			return True

		return False

# converter = Youtube2Spotify()
# q = 'Mild Orange - Some Feeling'
# playlist_id = converter.create_spotify_playlist('test', 'test desc', True)
# uri = converter.search_spotify(q)
# print(playlist_id, uri)
# converter.add_to_spotify(playlist_id, [uri])
