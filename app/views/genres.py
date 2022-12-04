from flask import request
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
    @genre_ns.doc(description='Get all genres', params={'page': 'Page number'}, responses={200: 'OK',
                                                                                           401: 'Unauthorized'})
    @auth_required
    def get() -> list[dict]:
        """This view return all genres by GET request"""
        page = int(request.args.get('page'))
        return genres_schema.dump(genre_service.get_genres(page)), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    @staticmethod
    @genre_ns.doc(description='Get one genre', params={'genre_id': 'Genre ID'}, responses={200: 'OK',
                                                                                           401: 'Unauthorized',
                                                                                           404: 'Not Found'})
    @auth_required
    def get(genre_id: int) -> str or dict:
        """This view return one genre filtered by genre_id by GET request"""
        genre = genre_service.get_genre(genre_id)
        if not genre:
            return 'genre not found', 404
        return genre_schema.dump(genre), 200
