import os
import time
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE = "https://api.spotify.com/v1"


class SpotifyClient:
    def __init__(self):
        self.session = requests.Session()
        self.access_token = None
        self.token_expires_at = 0

    # ------------------ AUTH ------------------
    def _get_access_token(self):
        """Fetch a new access token"""
        response = requests.post(
            SPOTIFY_TOKEN_URL,
            data={"grant_type": "client_credentials"},
            auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        self.access_token = data["access_token"]
        self.token_expires_at = time.time() + data["expires_in"] - 60

    def _get_headers(self):
        """Return valid auth headers"""
        if not self.access_token or time.time() >= self.token_expires_at:
            self._get_access_token()

        return {"Authorization": f"Bearer {self.access_token}"}

    # ------------------ CORE REQUEST ------------------
    def _get(self, endpoint, params=None):
        url = f"{SPOTIFY_API_BASE}{endpoint}"
        response = self.session.get(
            url,
            headers=self._get_headers(),
            params=params,
            timeout=10
        )
        response.raise_for_status()
        return response.json()

    # ------------------ SEARCH ------------------
    def search(self, query, search_type, limit=5):
        data = self._get(
            "/search",
            params={
                "q": query,
                "type": search_type,
                "limit": limit
            }
        )
        return data[f"{search_type}s"]["items"]

    def search_artist(self, name, limit=5):
        return self.search(name, "artist", limit)

    def search_track(self, name, limit=5):
        return self.search(name, "track", limit)

    def search_album(self, name, limit=5):
        return self.search(name, "album", limit)

    def search_by_genre(self, genre, search_type="track", limit=5):
        return self.search(f"genre:{genre}", search_type, limit)

    # ------------------ ARTIST ------------------
    def get_artist_top_tracks(self, artist_id, market="US"):
        data = self._get(
            f"/artists/{artist_id}/top-tracks",
            params={"market": market}
        )
        return data["tracks"]

    def get_artist_albums(self, artist_id, limit=10):
        data = self._get(
            f"/artists/{artist_id}/albums",
            params={"limit": limit}
        )
        return data["items"]

    # ------------------ TRACK ------------------
    def get_track_audio_features(self, track_id):
        return self._get(f"/audio-features/{track_id}")

    # ------------------ RECOMMENDATIONS ------------------
    def get_recommendations(self, seed_artists=None, seed_tracks=None, seed_genres=None, limit=10):
        return self._get(
            "/recommendations",
            params={
                "seed_artists": ",".join(seed_artists or []),
                "seed_tracks": ",".join(seed_tracks or []),
                "seed_genres": ",".join(seed_genres or []),
                "limit": limit
            }
        )["tracks"]
