import pytest

from app.services.director_service import DirectorService
from tests.conftest.conftest import director_dao


# ----------------------------------------------------------------
# test class of director service
class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao: director_dao):
        """
        Create an object of DirectorService
        :param director_dao:
        """
        self.director_service = DirectorService(director_dao)

    def test_get_directors(self):
        directors = self.director_service.get_directors()
        assert directors is not None, 'Error: no response from database'
        assert len(directors) > 1, 'Error: empty list of directors'

    def test_get_director(self):
        director = self.director_service.get_director(1)
        assert director is not None, 'Error: director not found'
        assert director.id is not None, 'Error: director not found'
        assert type(director.id) is int, 'Error: wrong type'
