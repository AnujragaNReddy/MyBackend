from fastapi import APIRouter

router = APIRouter(
    prefix="/music",
    tags=["Music"]
)

#------------------ MUSIC ROUTES ------------------
# Search Music by Title
# Search Music by Artist
# Search Music by Album
# Search Music by Genre
# Get Top Charts
# Get New Releases
# Get Playlists
# Create Playlist
# Add Track to Playlist