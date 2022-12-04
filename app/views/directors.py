from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.models import DirectorSchema
from configuration.auth_util import auth_required
from configuration.implemented import director_service


# ----------------------------------------------------------------
# create namespace and schemas to serialize/deserialize
director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


# ----------------------------------------------------------------
# views to handle directors requests
@director_ns.route('/')
class DirectorsView(Resource):
    @staticmethod
    @director_ns.doc(description='Get all directors', params={'page': 'Page number'}, responses={200: 'OK',
                                                                                                 401: 'Unauthorized'})
    @auth_required
    def get() -> list[dict]:
        """This view return all directors by GET request"""
        page = int(request.args.get('page'))
        return directors_schema.dump(director_service.get_directors(page)), 200


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    @staticmethod
    @director_ns.doc(description='Get one genre', params={'director_id': 'Director ID'}, responses={200: 'OK',
                                                                                                    401: 'Unauthorized',
                                                                                                    404: 'Not Found'})
    @auth_required
    def get(director_id: int) -> str or dict:
        """This view return one director filtered by director_id by GET request"""
        director = director_service.get_director(director_id)
        if not director:
            return 'director not found', 404
        return directors_schema.dump(director), 200
