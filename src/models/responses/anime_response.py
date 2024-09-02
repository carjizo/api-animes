from pydantic import BaseModel

class AnimeResponse(BaseModel):
    title: str
    episode: int
    links: list