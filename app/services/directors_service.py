from app.dao.director_dao import DirectorDAO


# ----------------------------------------------------------------
# DirectorService class with business logic to work with views and DirectorDAO
class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self):
        return self.director_dao.get_all_directors()

    def get_director(self, director_id):
        return self.director_dao.get_director_by_id(director_id)
