import requests
import json
from secrets import spotify_user_id, spotify_user_token, youtube_playlist_id, youtube_api_key


class Youtube2Spotify:
    def __init__(self):
        self.spotify_user_id = spotify_user_id
        self.spotify_user_token = spotify_user_token
        self.youtube_playlist_id = youtube_playlist_id
        self.youtube_api_key = youtube_api_key

        self.spotify_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.spotify_user_token}'
        }

    def create_spotify_playlist(self, pl_name, pl_desc, public=None):

        url = f'https://api.spotify.com/v1/users/{self.spotify_user_id}/playlists'

        data = json.dumps({
            'name': pl_name,
            'description': pl_desc,
            'public': public or True
        })

        response = requests.post(url, data=data, headers=self.spotify_headers)

        if response.status_code == 201:
            print("Created playlist successfully!")

            return response.json()['id']

    def search_spotify(self, query):
        url = 'https://api.spotify.com/v1/search'

        data = {
            'q': query,
            'type': 'track'
        }

        response = requests.get(url, params=data, headers=self.spotify_headers)

        if response.status_code == 200:
            songs = response.json()['tracks']['items']
            if len(songs):
                first_song_uri = songs[0]['uri']

                return first_song_uri

    def add_to_spotify(self, playlist_id, song_uris):
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

        data = json.dumps({
            'uris': song_uris,
        })

        response = requests.post(url, data=data, headers=self.spotify_headers)

        if response.status_code == 201:
            print("Songs added successfully!")
            return True

        return False

    def get_youtube_playlist(self):
        url = 'https://www.googleapis.com/youtube/v3/playlistItems'

        params = {
            'part': 'snippet',
            'playlistId': self.youtube_playlist_id,
            'key': self.youtube_api_key,
            'maxResults': 25
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            total_videos = len(response.json()['items'])
            print(f"The playlist has {total_videos} videos...")
            videos = response.json()['items']
            video_titles = []
            for video in videos:
                video_titles.append(video['snippet']['title'])

        return video_titles
