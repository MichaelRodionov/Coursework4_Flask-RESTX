from app.dao.models.models import Director


# ----------------------------------------------------------------
# DirectorDAO class to work with database
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        """
        Method to query all directors from database
        :return: all directors to DirectorService
        """
        directors = self.session.query(Director).all()
        return directors

    def get_director_by_id(self, director_id: int):
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
