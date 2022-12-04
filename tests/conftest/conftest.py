import pytest
from unittest.mock import MagicMock

from app.dao.movie_dao import MovieDAO
from app.dao.genre_dao import GenreDAO
from app.dao.director_dao import DirectorDAO
from app.dao.user_dao import UserDAO
from tests.conftest.test_data import ALL_MOVIES, MOVIE_BY_ID, ALL_DIRECTORS, DIRECTOR_BY_ID, \
    ALL_GENRES, GENRE_BY_ID, USER_BY_EMAIL


# ----------------------------------------------------------------
# Fixture to mock MovieDAO methods
@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie_dao.get_all_movies = MagicMock(return_value=ALL_MOVIES)
    movie_dao.get_movie_by_id = MagicMock(return_value=MOVIE_BY_ID)
    return movie_dao


# ----------------------------------------------------------------
# Fixture to mock DirectorDAO methods
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    director_dao.get_all_directors = MagicMock(return_value=ALL_DIRECTORS)
    director_dao.get_director_by_id = MagicMock(return_value=DIRECTOR_BY_ID)
    return director_dao


# ----------------------------------------------------------------
# Fixture to mock GenreDAO methods
@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre_dao.get_all_genres = MagicMock(return_value=ALL_GENRES)
    genre_dao.get_genre_by_id = MagicMock(return_value=GENRE_BY_ID)
    return genre_dao


# ----------------------------------------------------------------
# Fixture to mock UserDAO methods
@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)
    user_dao.get_user_by_email = MagicMock(return_value=USER_BY_EMAIL)
    user_dao.create_user = MagicMock()
    user_dao.update_user = MagicMock()
    return user_dao
