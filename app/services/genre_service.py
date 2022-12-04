from app.dao.genre_dao import GenreDAO
from app.dao.models.models import Genre


# ----------------------------------------------------------------
# GenreService class with business logic to work with views and GenreDAO
class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self, page=None) -> list:
        """
        Method to get all genres
        :return: list of genres
        """
        return self.genre_dao.get_all_genres(page)

    def get_genre(self, genre_id: int) -> Genre:
        """
        Method to  get genre by genre id
        :param genre_id: Genre ID
        :return: Genre object
        """
        return self.genre_dao.get_genre_by_id(genre_id)
