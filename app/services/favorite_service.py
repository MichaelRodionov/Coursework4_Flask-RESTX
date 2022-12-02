from app.dao.favorite_dao import FavoriteDAO
from app.services.user_service import secure_service


# ----------------------------------------------------------------
# FavoriteService class with business logic to work with views and FavoriteDAO
class FavoriteService:
    def __init__(self, favorite_dao: FavoriteDAO):
        self.fav_dao = favorite_dao

    def get_favorites(self) -> list[dict]:
        """
        Method to get user_id from token and send it to favorite dao
        :return: list of favorite movies filtered by user id
        """
        user_id = secure_service.get_email_or_id_from_token(is_id=True)
        return self.fav_dao.get_all_favorites(user_id)

    def add_movie_to_favorite(self, mid: int) -> None:
        """
        Method to get user_id from token and add favorite movie to this user
        :param mid: movie id
        :return: None
        """
        user_id = secure_service.get_email_or_id_from_token(is_id=True)
        data = {
            "user_id": user_id,
            "movie_id": mid
        }
        self.fav_dao.add_favorite_movie(data)

    def remove_movie_from_favorite(self, mid: int) -> None:
        """
        Method to get user_id from token and delete movie from users favorites
        :param mid: movie id
        :return: None
        """
        self.fav_dao.delete_movie_from_favorite(mid)
