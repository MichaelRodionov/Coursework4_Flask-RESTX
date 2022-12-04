from app.dao.models.models import Favorite, Movie


# ----------------------------------------------------------------
# FavoritesDAO to work with database
class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def get_all_favorites(self, uid: int) -> list:
        """
        Method to query all favorites of user
        :param uid: user id
        :return: list of favorite movies
        """
        return self.session.query(Movie.title, Movie.rating, Movie.year, Movie.trailer, Movie.description).\
            join(Favorite, Favorite.movie_id == Movie.id).filter(Favorite.user_id == uid)

    def add_favorite_movie(self, data: dict) -> None:
        """
        Method to add a new movie to favorites
        :param data: user id and movie id database
        :return: None
        """
        new_favorite = Favorite(**data)
        self.session.add(new_favorite)
        self.session.commit()

    def delete_movie_from_favorite(self, mid: int) -> None:
        """
        Method to delete a movie from favorites
        :param mid: movie id
        :return: None
        """
        movie_to_delete = self.session.query(Favorite).filter(Favorite.movie_id == mid).first()
        self.session.delete(movie_to_delete)
        self.session.commit()
