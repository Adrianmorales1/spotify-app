import requests

SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/adrianmorales2635/playlists'
ACCESS_TOKEN = "BQBJD-hln7Br5khw9oAC8Q2KZytd-puvHmH5TV6GIVCSRMPkx2ZeVr79v7uDeG6n17GqAjbb3W510_UVsUsny7nNuNO74Zz6_DS1aT4i0H5MsiPb138soahpQYCpABxh__9VLexZngg3kAmSeNH-pQHqT7cc13ykxTxnLfrKR-kSiDr1g9y_tVBfuT3qqW1MO1lXH0Flmchp5JSe0dSOwNj6VamVS9pgxWFMj2xAxmZOi0cgpiV68w"

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL, headers= {
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json= {
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp

def main():
    playlist = create_playlist_on_spotify(
        name= "API Playlist",
        public = True
    )
    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()