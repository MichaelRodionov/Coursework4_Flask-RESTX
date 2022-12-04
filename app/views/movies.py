from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.models import MovieSchema
from constants import DOC_PARAMS
from helpers import auth_required
from implemented import movie_service


# ----------------------------------------------------------------
# create namespace and schemas to serialize/deserialize
movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


# ----------------------------------------------------------------
# views to handle movies requests
@movie_ns.route('/')
class MoviesView(Resource):
    @staticmethod
    @movie_ns.doc(description='Get all movies', params=DOC_PARAMS, responses={200: 'OK', 401: 'Unauthorized'})
    @auth_required
    def get() -> list[dict]:
        """This view returns all movies by pages or sort movies by director/genre/year by GET request"""
        filter_params = {
            "director_id": request.args.get('director_id'),
            "genre_id": request.args.get('genre_id'),
            "year": request.args.get('year'),
            "page": request.args.get('page'),
            "status": request.args.get('status')
        }
        return movies_schema.dump(movie_service.get_movies(filter_params)), 200


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    @staticmethod
    @movie_ns.doc(description='Get one movie', params={'movie_id': 'Movie ID'}, responses={200: 'OK',
                                                                                           401: 'Unauthorized',
                                                                                           404: 'Not Found'})
    @auth_required
    def get(movie_id: int) -> str or dict:
        """This view return one movie filtered by movie_id by GET request"""
        movie = movie_service.get_one_movie(movie_id)
        if not movie:
            return 'movie not found', 404
        return movie_schema.dump(movie), 200
