from app.dao.user_dao import UserDAO
from app.services.secure_service import SecureService


# ----------------------------------------------------------------
# create secure_service object
secure_service = SecureService()


# ----------------------------------------------------------------
# UserService class to work with views and UserDAO
class UserService:
    """Service is needed to work with users views and UserDAO"""
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_user_page(self):
        """
        Method to get user data with available attributes
        :return: User with available attributes
        """
        user_id = secure_service.get_id_from_token()
        return self.user_dao.get_user_page(user_id)

    def create_user(self, data: dict):
        """
        Method to create new user
        :param data: dict with name, surname, email, password, favorite_genre
        :return: None
        """
        return self.user_dao.create_user(data)

    def get_user_by_id(self, uid: int):
        """
        Method to filter user by user_id (uid)
        :param uid: user id
        :return: User filtered by user_id
        """
        return self.user_dao.get_user_by_id(uid)

    def get_user_by_email(self, email: str):
        """
        Method to filter user by email
        :param email: user email
        :return: User filtered by email
        """
        return self.user_dao.get_user_by_email(email)

    def update_user(self, data: dict):
        """
        Method to update user info such as name, surname, favorite_genre
        :param data: dict with name/surname/favorite_genre
        :return: None
        """
        user = self.user_dao.get_user_by_id(secure_service.get_id_from_token())
        if "name" in data:
            user.name = data.get("name")
        if "surname" in data:
            user.surname = data.get("surname")
        if "favorite_genre" in data:
            user.favorite_genre = data.get("favorite_genre")
        return self.user_dao.update_user(user)

    def update_password(self, passwords: dict):
        """
        Method to update user password
        :param passwords:
        :return: None
        """
        password_1, password_2 = passwords.get("password_1"), passwords.get("password_2")
        user = self.get_user_by_id(secure_service.get_id_from_token())
        if not secure_service.compare_passwords(user.password, password_1):
            return "Incorrect password", 400
        user.password = secure_service.make_user_password_hash(password_2)
        return self.user_dao.update_user(user)
