from src.models.responses.anime_response import AnimeResponse
from src.models.request.anime_request import AnimeRequest
from src.client.AnimeFLV import AnimeFLVClient
from src.models.dto.anime_dto import AnimeDTO

class AnimeService():
    """ AnimeService docs """
    def get_links(anime: AnimeRequest) -> AnimeResponse:
        kwargs:dict = {}
        kwargs['title'] = anime.id
        kwargs['episode'] = anime.episode
        kwargs['links'] = AnimeFLVClient().get_links(anime=anime)
        return AnimeResponse(**kwargs)
    
    def find_by_name(name_anime: str) -> list[AnimeDTO]:
        animes: list = []
        animes_by_name = AnimeFLVClient().search(name_anime=name_anime)
        for anime in animes_by_name:
            kwargs: dict = {}
            kwargs['id'] = anime.id
            kwargs['title'] = anime.title
            kwargs['synopsis'] = anime.synopsis
            kwargs['rating'] = anime.rating
            kwargs['genres'] = anime.genres
            kwargs['type'] = anime.type
            kwargs['debut'] = anime.debut
            animes.append(AnimeDTO(**kwargs))
        return animes