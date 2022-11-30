from sqlalchemy import desc

from constants import LIMIT_VALUE, OFFSET_VALUE
from app.dao.models.models import Movie


# ----------------------------------------------------------------
# MovieDAO class to work with database
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self, director_id=None, genre_id=None, year=0, page=None, status=None):
        """
        This function is called to query all movies or movies sorted by Director or/and Genre
        :return: all movies or movies sorted by director/genre/year to MovieService
        """
        movies_query = self.session.query(Movie)
        if director_id is not None:
            movies_query = movies_query.filter(Movie.director_id == director_id)
        if genre_id is not None:
            movies_query = movies_query.filter(Movie.genre_id == genre_id)
        if year is not None:
            movies_query = movies_query.filter(Movie.year == year)
        if status is not None and status == 'new':
            movies_query = movies_query.order_by(desc(Movie.id))
        else:
            if page and int(page) > 0:
                movies_query = movies_query.limit(LIMIT_VALUE).offset(OFFSET_VALUE * (int(page) - 1))
        return movies_query.all()

    def get_movie_by_id(self, movie_id):
        """
        This function is called to query movie from database by movie_id
        :param movie_id:
        :return: return movie by movie_id to MovieService
        """
        try:
            movie_by_id = self.session.query(Movie).get(movie_id)
            return movie_by_id
        except Exception as e:
            return str(e)
