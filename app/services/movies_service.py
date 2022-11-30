from flask import request

from app.dao.movie_dao import MovieDAO


# ----------------------------------------------------------------
# MovieService class with business logic to work with views and MovieDAO
class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list:
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        page = request.args.get('page')
        status = request.args.get('status')
        return self.movie_dao.get_all_movies(director_id, genre_id, year, page, status)

    def get_one_movie(self, movie_id: int):
        return self.movie_dao.get_movie_by_id(movie_id)
