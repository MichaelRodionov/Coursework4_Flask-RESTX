from app.dao.genre_dao import GenreDAO


# ----------------------------------------------------------------
# GenreService class with business logic to work with views and GenreDAO
class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self):
        return self.genre_dao.get_all_genres()

    def get_genre(self, genre_id):
        return self.genre_dao.get_genre_by_id(genre_id)
