from app.dao.models.models import Genre
from configuration.constants import LIMIT_VALUE, OFFSET_VALUE


# ----------------------------------------------------------------
# GenreDAO class to work with database
class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self, page=None) -> list:
        """
        Method to query all genres from database
        :param: page number
        :return: all genres to GenreService
        """
        genres_query = self.session.query(Genre)
        if page and page > 0:
            genres_query = genres_query.limit(LIMIT_VALUE).offset(OFFSET_VALUE * (page - 1))
        return genres_query.all()

    def get_genre_by_id(self, genre_id: int) -> Genre:
        """
        Method to query genre from database by genre id
        :param genre_id:
        :return: genre by genre id to GenreService
        """
        try:
            genre = self.session.query(Genre).get(genre_id)
            return genre
        except Exception as e:
            return str(e)
