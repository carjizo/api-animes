from pydantic import BaseModel, Field
from typing import Union

class AnimeRequest(BaseModel):
    id: Union[str, int]
    episode: int = Field(le=5000)

    class Config:
        schema_extra = {
            "example": {
                "id": "naruto",
                "episode": 1
            }
        }