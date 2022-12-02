from app.dao.director_dao import DirectorDAO


# ----------------------------------------------------------------
# DirectorService class with business logic to work with views and DirectorDAO
class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> list[dict]:
        """
        Method to get all directors
        :return: list  of directors
        """
        return self.director_dao.get_all_directors()

    def get_director(self, director_id) -> dict:
        """
        Method to get director by director id
        :param director_id:
        :return: one director
        """
        return self.director_dao.get_director_by_id(director_id)
