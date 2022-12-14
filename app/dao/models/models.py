from marshmallow import Schema, fields

from database.setup_db import db


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
# User model and schema to serialization/deserialization
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String, default=None)
    surname = db.Column(db.String, default=None)
    favourite_genre = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre')


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favourite_genre = fields.Int()


# ----------------------------------------------------------------
# Favorite model
class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer(), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie = db.relationship('Movie')
    user = db.relationship('User')
