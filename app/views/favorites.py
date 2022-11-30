from flask_restx import Resource, Namespace

from app.dao.models.models import UserMovieSchema
from app.services.secure_service import get_id_from_token
from helpers import auth_required
from implemented import movie_service

# ----------------------------------------------------------------
# create namespace
fav_ns = Namespace('favorites/movies')
user_movie_schema = UserMovieSchema()


# ----------------------------------------------------------------
# views to handle favorites requests
@fav_ns.route('/<int: mid>/')
class FavoritesViews(Resource):
    @staticmethod
    @auth_required
    def post(mid):
        user_movie = {
            "user_id": get_id_from_token(),
            "movie_id": movie_service.get_one_movie(mid)
        }

        user_movie_schema.dump()