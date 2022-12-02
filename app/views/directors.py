from flask_restx import Resource, Namespace

from app.dao.models.models import DirectorSchema
from helpers import auth_required
from implemented import director_service


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
    @auth_required
    def get():
        """This view return all directors by GET request"""
        return directors_schema.dump(director_service.get_directors()), 200


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    @staticmethod
    @auth_required
    def get(director_id):
        """This view return one director filtered by director_id by GET request"""
        return directors_schema.dump(director_service.get_director(director_id)), 200
