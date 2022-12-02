from app.dao.genre_dao import GenreDAO


# ----------------------------------------------------------------
# GenreService class with business logic to work with views and GenreDAO
class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self) -> list[dict]:
        """
        Method to get all genres
        :return: list of genres
        """
        return self.genre_dao.get_all_genres()

    def get_genre(self, genre_id) -> dict:
        """
        Method to  get genre by genre id
        :param genre_id:
        :return: one genre
        """
        return self.genre_dao.get_genre_by_id(genre_id)
