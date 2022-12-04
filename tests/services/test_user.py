import pytest

from app.services.user_service import UserService
from tests.conftest.conftest import user_dao
from tests.conftest.test_data import TEST_EMAIL


# ----------------------------------------------------------------
# test class of user service
class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao: user_dao):
        """
        Create an object of UserService
        :param user_dao:
        """
        self.user_service = UserService(user_dao)

    def test_get_user_by_email(self):
        email = TEST_EMAIL
        user = self.user_service.get_user_by_email(email)
        assert user is not None, 'Error: no response'
        assert user.email == email, 'Error: wrong email'

