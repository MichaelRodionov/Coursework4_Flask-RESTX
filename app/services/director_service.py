from app.dao.director_dao import DirectorDAO
from app.dao.models.models import Director


# ----------------------------------------------------------------
# DirectorService class with business logic to work with views and DirectorDAO
class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self, page=None) -> list:
        """
        Method to get all directors
        :return: list  of directors
        """
        return self.director_dao.get_all_directors(page)

    def get_director(self, director_id: int) -> Director:
        """
        Method to get director by director id
        :param director_id:
        :return: Director object
        """
        return self.director_dao.get_director_by_id(director_id)
