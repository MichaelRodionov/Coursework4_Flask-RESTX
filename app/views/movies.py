from flask_restx import Resource, Namespace

from app.dao.models.models import MovieSchema
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
    # @auth_required
    def get():
        """This view returns all movies by pages or sort movies by director/genre/year by GET request"""
        return movies_schema.dump(movie_service.get_movies()), 200


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    @staticmethod
    # @auth_required
    def get(movie_id):
        """This view return one movie filtered by movie_id by GET request"""
        movie = movie_service.get_one_movie(movie_id)
        if not movie:
            return 'movie not found', 404
        return movie_schema.dump(movie), 200
