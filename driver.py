from main import Youtube2Spotify

print("\n## Youtube2Spotify - Convert YT playlist to Spotify ##\n\n")

pl_name = input("Enter new Spotify playlist's name: ")
pl_desc = input("Enter playlist description: ")

print("\n")

converter = Youtube2Spotify()

spotify_playlist_id = converter.create_spotify_playlist(pl_name, pl_desc)

yt_vid_titles = converter.get_youtube_playlist()

spotify_song_uris = [] 

for video in yt_vid_titles:
    uri = converter.search_spotify(video)
    if uri:
        spotify_song_uris.append(uri)

converter.add_to_spotify(spotify_playlist_id, spotify_song_uris)
