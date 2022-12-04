from app.dao.models.models import Director
from configuration.constants import LIMIT_VALUE, OFFSET_VALUE


# ----------------------------------------------------------------
# DirectorDAO class to work with database
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self, page=None) -> list:
        """
        Method to query all directors from database
        :return: all directors to DirectorService
        """
        directors_query = self.session.query(Director)
        if page and page > 0:
            directors_query = directors_query.limit(LIMIT_VALUE).offset(OFFSET_VALUE * (page - 1))
        return directors_query.all()

    def get_director_by_id(self, director_id: int) -> Director:
        """
        Method to query director from database by director id
        :param director_id:
        :return: director by director id to DirectorService
        """
        try:
            director_by_id = self.session.query(Director).get(director_id)
            return director_by_id
        except Exception as e:
            return str(e)
