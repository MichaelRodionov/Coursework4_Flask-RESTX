from app.dao.director_dao import DirectorDAO
from app.dao.favorite_dao import FavoriteDAO
from app.dao.genre_dao import GenreDAO
from app.dao.movie_dao import MovieDAO
from app.dao.user_dao import UserDAO
from app.services.auth_service import AuthService
from app.services.favorite_service import FavoriteService
from app.services.movies_service import MovieService
from app.services.directors_service import DirectorService
from app.services.genres_service import GenreService
from app.services.user_service import UserService
from setup_db import db

# ----------------------------------------------------------------
# creating objects of dao and services
movie_dao = MovieDAO(db.session)
director_dao = DirectorDAO(db.session)
genre_dao = GenreDAO(db.session)
user_dao = UserDAO(db.session)
user_movie_dao = FavoriteDAO(db.session)

movie_service = MovieService(movie_dao)
director_service = DirectorService(director_dao)
genre_service = GenreService(genre_dao)
user_service = UserService(user_dao)
auth_service = AuthService(user_service)
favorite_service = FavoriteService(user_movie_dao)
