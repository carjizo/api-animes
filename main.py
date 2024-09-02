from src.middlewares.error_handler import ErrorHandler
from src.controllers.anime_controller import AnimeController

from fastapi import FastAPI

app = FastAPI()
app.title = "Mi API Animes"
app.version = "0.0.1"
app.add_middleware(ErrorHandler)
app.include_router(AnimeController.anime_controller)