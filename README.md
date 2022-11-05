# spotify-last-thirty-likes

Creates a new playlist from your last 30 liked songs on Spotify.


## Installation

1. Clone this repository
2. `poetry install --no-dev`

## Usage

1. Create a new app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)
2. Export variables for `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` (**N.B.** `PY` not `FY` in `SPOTIPY_CLI…`)
3. `poetry run python app.py`
