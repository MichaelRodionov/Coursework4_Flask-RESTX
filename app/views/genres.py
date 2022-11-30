from flask_restx import Resource, Namespace

from app.dao.models.models import GenreSchema
from helpers import auth_required
from implemented import genre_service


# ----------------------------------------------------------------
# create namespace and schemas to serialize/deserialize
genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


# ----------------------------------------------------------------
# views to handle genres requests
@genre_ns.route('/')
class GenresView(Resource):
    @staticmethod
    # @auth_required
    def get():
        """This view return all genres by GET request"""
        return genres_schema.dump(genre_service.get_genres()), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    @staticmethod
    # @auth_required
    def get(genre_id):
        """This view return one genre filtered by genre_id by GET request"""
        return genre_schema.dump(genre_service.get_genre(genre_id)), 200
