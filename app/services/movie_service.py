from flask import request

from app.dao.models.models import Movie
from app.dao.movie_dao import MovieDAO


# ----------------------------------------------------------------
# MovieService class with business logic to work with views and MovieDAO
class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self, filter_params=None) -> list:
        """
        Method to get all movies
        :return: list of  movies
        """
        return self.movie_dao.get_all_movies(filter_params)

    def get_one_movie(self, movie_id: int) -> Movie:
        """
        Method to get movie by movie id
        :param movie_id:
        :return: Movie object
        """
        return self.movie_dao.get_movie_by_id(movie_id)
