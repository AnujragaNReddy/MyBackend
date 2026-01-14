
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import routes, books_routes, spotify_client_apis, music_routes

app = FastAPI()

# Allow CORS for frontend (localhost:5173)
app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:5173"],
	allow_credentials=True,
	allow_methods=["*"] ,
	allow_headers=["*"] ,
)

app.include_router(routes.router)
app.include_router(books_routes.router)
app.include_router(spotify_client_apis.router)
app.include_router(music_routes.router)
