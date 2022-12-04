import pytest

from app.services.auth_service import AuthService
from implemented import user_service
from tests.conftest.test_data import AUTH_DATA, TEST_PASSWORD_HASH


class TestAuthService:
    @pytest.fixture(autouse=True)
    def auth_service(self):
        self.auth_service = AuthService(user_service)

    def test_convert_user_password_to_hash(self, data=AUTH_DATA):
        str_password = data['password']
        converted_data = self.auth_service.convert_user_password_to_hash(data)
        assert type(converted_data['password']) is bytes, 'Error: wrong encode'
        assert converted_data['password'] == TEST_PASSWORD_HASH, 'Error: wrong encode'
        assert converted_data['password'] != str_password, 'Error: wrong encode'
