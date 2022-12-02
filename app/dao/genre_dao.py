from app.dao.models.models import Genre


# ----------------------------------------------------------------
# GenreDAO class to work with database
class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        """
        Method to query all genres from database
        :return: all genres to GenreService
        """
        genres = self.session.query(Genre).all()
        return genres

    def get_genre_by_id(self, genre_id: int):
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
