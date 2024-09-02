from src.models.request.anime_request import AnimeRequest

from animeflv import AnimeFLV
from animeflv.animeflv import AnimeFLVParseError

class AnimeFLVClient():
    """ AnimeFLVClient docs """
    def __init__(self):
        super(AnimeFLVClient, self).__init__()

    def get_links(self, anime: AnimeRequest) -> list:
        try:
            info = AnimeFLV().get_links(id=anime.id, episode=anime.episode)
        except AnimeFLVParseError:
            return []
        return [i.url for i in info]
        
    def search(self, name_anime: str) -> list:
        return AnimeFLV().search(query=name_anime)