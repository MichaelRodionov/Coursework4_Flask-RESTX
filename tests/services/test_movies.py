import pytest

from app.services.movie_service import MovieService
from tests.conftest.conftest import movie_dao


# ----------------------------------------------------------------
# test class of movie service
class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao: movie_dao):
        """
        Create an object of MovieService
        :param movie_dao:
        """
        self.movie_service = MovieService(movie_dao)

    def test_get_all_movies(self):
        """
        Method to test get_all_movies method of movie service
        """
        movies = self.movie_service.get_movies(filter_params=None)
        assert movies is not None, 'Error: no response from database'
        assert len(movies) > 1, 'Error: empty list of movies'

    def test_get_movie_by_id(self):
        """
        Method to test get_movie_by_id method of movie service
        """
        movie = self.movie_service.get_one_movie(1)
        assert movie is not None, 'Error: movie not found'
        assert movie.id == 1, 'Error: wrong movie id'
        assert movie.id is not None, 'Error: movie not found'
        assert type(movie.id) is int, 'Error: wrong type'
        assert movie.title == 'test_film_1', 'Error: wrong movie title'
