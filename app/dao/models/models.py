from marshmallow import Schema, fields

from setup_db import db


# ----------------------------------------------------------------
# Movie model and schema to serialization/deserialization
class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = db.relationship('Director')


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


# ----------------------------------------------------------------
# Director model and schema to serialization/deserialization
class Director(db.Model):
    __tablename__ = 'director'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


# ----------------------------------------------------------------
# Genre model and schema to serialization/deserialization
class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


# ----------------------------------------------------------------
# secondary table  to create many-to-many relationship between table 'user' and table 'genre'
user_movie = db.Table('user_movie',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                      db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True))


# ----------------------------------------------------------------
# User model and schema to serialization/deserialization
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String, default=None)
    surname = db.Column(db.String, default=None)
    favorite_genre = db.Column(db.Integer, db.ForeignKey('genre.id'), default=None)
    genre = db.relationship('Genre')
    movie = db.relationship('Movie', secondary=user_movie, backref=db.backref('users'))


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    password = fields.Str()
    favorite_genre = fields.Int()

