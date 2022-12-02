from app.dao.models.models import User


# ----------------------------------------------------------------
# UserDAO class to work with database
class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_user_page(self, uemail):
        """
        This method is needed to query available user info from database
        :param uemail:
        :return: User with name, surname, email, favorite_genre attributes
        """
        return self.session.query(User.name, User.surname, User.email, User.favorite_genre).filter(User.email == uemail).first()

    def get_user_by_email(self, email):
        """
        This method is needed to query user by username
        :param email:
        :return: user object
        """
        return self.session.query(User).filter(User.email == email).first()

    def create_user(self, data):
        """
        This method is needed to add a new user to the database
        :param data:
        :return: user_id
        """
        user = User(**data)
        self.session.add(user)
        self.session.commit()

    def update_user(self, user):
        """
        This method is needed to overwrite user with updated attributes
        :param user:
        """
        self.session.add(user)
        self.session.commit()
