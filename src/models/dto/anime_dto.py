from pydantic import BaseModel
from typing import List, Optional, Union

class AnimeDTO(BaseModel):
    id: Union[str, int]
    title: str
    synopsis: Optional[str] = None
    rating: Optional[str] = None
    genres: Optional[List[str]] = None
    debut: Optional[str] = None
    type: Optional[str] = None