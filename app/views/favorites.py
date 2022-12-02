from flask_restx import Resource, Namespace

from app.views.movies import movies_schema
from helpers import auth_required
from implemented import favorite_service


# ----------------------------------------------------------------
# create namespace
fav_ns = Namespace('favorites/movies')


# ----------------------------------------------------------------
# views to handle favorites requests
@fav_ns.route('/')
class FavoritesViews(Resource):
    @staticmethod
    @auth_required
    def get() -> list[dict]:
        """This view is needed to get all users favorites"""
        return movies_schema.dump(favorite_service.get_favorites()), 200


@fav_ns.route('/<int:mid>')
class FavoriteViews(Resource):
    @staticmethod
    @auth_required
    def post(mid) -> str:
        """This view is needed to add movie by movie id to favorites"""
        favorite_service.add_movie_to_favorite(mid)
        return "", 201

    @staticmethod
    @auth_required
    def delete(mid) -> str:
        """This view is needed to remove movie by movie id from favorites"""
        favorite_service.remove_movie_from_favorite(mid)
        return "", 204
