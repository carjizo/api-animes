from src.models.request.anime_request import AnimeRequest
from src.models.responses.anime_response import AnimeResponse
from src.services.anime_service import AnimeService
from src.models.dto.anime_dto import AnimeDTO

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class AnimeController():
    """ AnimeRouter docs """
    anime_controller = APIRouter()

    @anime_controller.post('/links', tags=['animes'], response_model=list[AnimeResponse], status_code=200)
    def get_links(anime: AnimeRequest):
        """
        Get likns server animes\n
        parameter id: id del anime\n
        parameter episode: número de episodios
        """
        links = AnimeService.get_links(anime)
        return JSONResponse(status_code=200, content=jsonable_encoder(links))
    
    @anime_controller.get('/find-by-name/{name_anime}', tags=['animes'], response_model=list[AnimeDTO], status_code=200)
    def find_by_anime(name_anime: str):
        """
        Find by name anime\n
        parameter name_anime: nombre random de algún anime
        """
        animes = AnimeService.find_by_name(name_anime)
        return JSONResponse(status_code=200, content=jsonable_encoder(animes))