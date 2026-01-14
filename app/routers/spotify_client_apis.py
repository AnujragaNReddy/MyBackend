from fastapi import APIRouter, Depends, HTTPException
from app.services.spotify_client import SpotifyClient

router = APIRouter(
    prefix="/spotify",
    tags=["Music-Spotify"]
)

def get_spotify():
    return SpotifyClient()

# ------------------ SEARCH ------------------

@router.get("/search/track")
def search_track(
    q: str,
    limit: int = 5,
    spotify: SpotifyClient = Depends(get_spotify)
):
    try:
        return spotify.search_track(q, limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/search/artist")
def search_artist(
    q: str,
    limit: int = 5,
    spotify: SpotifyClient = Depends(get_spotify)
):
    try:
        return spotify.search_artist(q, limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/search/album")
def search_album(
    q: str,
    limit: int = 5,
    spotify: SpotifyClient = Depends(get_spotify)
):
    try:
        return spotify.search_album(q, limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/search/genre")
def search_by_genre(
    genre: str,
    type: str = "track",
    limit: int = 5,
    spotify: SpotifyClient = Depends(get_spotify)
):
    try:
        return spotify.search_by_genre(genre, type, limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ------------------ ARTIST ------------------

@router.get("/artist/{artist_id}/top-tracks")
def artist_top_tracks(
    artist_id: str,
    market: str = "US",
    spotify: SpotifyClient = Depends(get_spotify)
):
    try:
        return spotify.get_artist_top_tracks(artist_id, market)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/artist/{artist_id}/albums")
def artist_albums(
    artist_id: str,
    limit: int = 10,
    spotify: SpotifyClient = Depends(get_spotify)
):
    try:
        return spotify.get_artist_albums(artist_id, limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ------------------ TRACK ------------------

@router.get("/track/{track_id}/audio-features")
def track_audio_features(
    track_id: str,
    spotify: SpotifyClient = Depends(get_spotify)
):
    try:
        return spotify.get_track_audio_features(track_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ------------------ RECOMMENDATIONS ------------------

@router.get("/recommendations")
def recommendations(
    seed_artists: str | None = None,
    seed_tracks: str | None = None,
    seed_genres: str | None = None,
    limit: int = 10,
    spotify: SpotifyClient = Depends(get_spotify)
):
    try:
        return spotify.get_recommendations(
            seed_artists.split(",") if seed_artists else None,
            seed_tracks.split(",") if seed_tracks else None,
            seed_genres.split(",") if seed_genres else None,
            limit
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
