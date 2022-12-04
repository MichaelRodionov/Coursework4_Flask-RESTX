from sqlalchemy import desc

from constants import LIMIT_VALUE, OFFSET_VALUE
from app.dao.models.models import Movie


# ----------------------------------------------------------------
# MovieDAO class to work with database
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self, params=None) -> list:
        """
        Method to query all movies or movies sorted by Director or/and Genre
        :return: all movies or movies sorted by director/genre/year to MovieService
        """
        movies_query = self.session.query(Movie)
        if params.get('director_id') is not None:
            movies_query = movies_query.filter(Movie.director_id == params.get('director_id'))
        if params.get('genre_id') is not None:
            movies_query = movies_query.filter(Movie.genre_id == params.get('genre_id'))
        if params.get('year') is not None:
            movies_query = movies_query.filter(Movie.year == params.get('year'))
        if params.get('status') is not None and params.get('status') == 'new':
            movies_query = movies_query.order_by(desc(Movie.id))
        else:
            if params.get('page') and int(params.get('page')) > 0:
                movies_query = movies_query.limit(LIMIT_VALUE).offset(OFFSET_VALUE * (int(params.get('page')) - 1))
        return movies_query.all()

    def get_movie_by_id(self, movie_id: int) -> Movie:
        """
        Method to query movie from database by movie_id
        :param movie_id:
        :return: return movie by movie_id to MovieService
        """
        try:
            movie_by_id = self.session.query(Movie).get(movie_id)
            return movie_by_id
        except Exception as e:
            return str(e)
