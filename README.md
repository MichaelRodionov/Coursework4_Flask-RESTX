# Coursework 4. API development with Flask
___
## Project description:
✅ Authentication   
- **POST request**  ***/auth/register/*** - route to register user is system   
- **POST request**  ***/auth/login/*** - route to log user in system   
- **PUT request**  ***/auth/login/*** - route to update tokens   

✅ Users   
- **GET request**  ***/user/*** - route to open users page   
- **PATCH request**  ***/user/*** - route to update users info, such as name, surname, favorite genre   
- **PUT request**  ***/user/*** - route to update users password   

✅ Favorites   
- **GET request**  ***/favorites/movies/*** - route to open users favorite movies   
- **POST request**  ***/favorites/movies/<<int:movie_id>>*** - route to add movie to users favorites  
- **DELETE request**  ***/favorites/movies/<<int:movie_id>>*** - route to delete movie from users favorites   

✅ Movies   
- **GET request**  ***/movies/*** - route to get all movies (params - director_id, genre_id, year, status, page)   
- **GET request**  ***/movies/<<int:movie_id>>*** - route to get one movie   

✅ Directors   
- **GET request**  ***/directors/*** - route to get all directors (params - page)   
- **GET request**  ***/directors/<<int:director_id>>*** - route to get one director   

✅ Genres   
- **GET request**  ***/genres/*** - route to get all genres (params - page)   
- **GET request**  ***/genres/<<int:genre_id>>*** - route to get one genre
___
## Done:
✔️ Business logic located in services   
✔️ DAO layer around models   
✔️ Models contains necessary fields   
✔️ Relations in models are established   
✔️ Status codes returned according to REST rules   
✔️ Swagger documentation according to flask_restx documentation
