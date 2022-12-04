import pytest

from app.services.secure_service import SecureService
from tests.conftest.test_data import TEST_PASSWORD, TEST_PASSWORD_HASH


# ----------------------------------------------------------------
# test class of secure_service
class TestSecureService:
    @pytest.fixture(autouse=True)
    def secure_service(self):
        """
        Create an object of SecureService
        """
        self.secure_service = SecureService()

    def test_make_user_password_hash(self):
        hash_password = self.secure_service.make_user_password_hash(TEST_PASSWORD)
        assert hash_password is not None, 'Error: no response'
        assert TEST_PASSWORD != hash_password, 'Error: wrong encode'
        assert type(hash_password) == bytes, 'Error: wrong encode'

    def test_compare_passwords(self):
        comparing_result = self.secure_service.compare_passwords(TEST_PASSWORD_HASH, TEST_PASSWORD)
        assert type(comparing_result) is bool, 'Error: wrong type'
        assert comparing_result is True, 'Error: wrong result'
