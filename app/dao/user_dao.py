from app.dao.models.models import User


# ----------------------------------------------------------------
# UserDAO class to work with database
class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_user_page(self, email: str) -> User:
        """
        Method to query available user info from database
        :param email:
        :return: User with name, surname, email, favorite_genre attributes
        """
        return self.session.query(User.name, User.surname, User.email, User.favorite_genre).filter(User.email == email).first()

    def get_user_by_email(self, email: str) -> User:
        """
        Method to query user by username
        :param email:
        :return: user object
        """
        return self.session.query(User).filter(User.email == email).first()

    def create_user(self, data: dict) -> None:
        """
        Method to add a new user to the database
        :param data:
        :return: user_id
        """
        user = User(**data)
        self.session.add(user)
        self.session.commit()

    def update_user(self, data, email) -> None:
        """
        Method to overwrite user with updated attributes
        :param data:
        :param email
        """
        self.session.query(User).filter(User.email == email).update(data)
        self.session.commit()
