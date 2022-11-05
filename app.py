from itertools import islice
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPE = ["user-library-read", "playlist-modify-public"]


def forever(client, request):
    while request:
        yield from request["items"]

        if request["next"]:
            request = client.next(request)
        else:
            request = None


def _get_or_create_playlist(client: spotipy.Spotify, user_id: str, name: str) -> str:
    playlists = client.user_playlists(user_id)

    for pl in forever(client, playlists):
        if pl["name"] == name:
            return pl["id"]

    return client.user_playlist_create(user_id, name)["id"]


def main(playlist_size: int = 30, playlist_name: str = "Recently Liked"):
    client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    # Get the current user
    user_id = client.me()["id"]

    # Find the user's Starred playlist
    starred_playlist = client.current_user_saved_tracks(limit=min(playlist_size, 50))

    # Get or create a new playlist, `Recently Starred`
    target_playlist_id = _get_or_create_playlist(client, user_id, playlist_name)

    # Replace the playlist's contents with the user's starred tracks
    tracks = [
        item["track"]["uri"]
        for item in islice(forever(client, starred_playlist), playlist_size)
    ]
    client.playlist_replace_items(target_playlist_id, tracks)


if __name__ == "__main__":
    main()
