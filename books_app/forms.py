from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import Audience, Book, Author, Genre

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    publish_date = DateField('Date Published', validators=[DataRequired()])
    author = QuerySelectField('Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')

    def validate_title(form, field):
        if 'banana' in field.data:
            raise ValidationError('Title cannot contain the word banana')


class AuthorForm(FlaskForm):
    """Form to create an author."""
    name = StringField('Author Name',
        validators=[
            DataRequired(),
            Length(min=3, max=80, message="Name must be between 3 and 80 chacracters")
        ])
    biography = TextAreaField('Biography',
        validators=[
            DataRequired(),
            Length(min=10, max=500, message="Biography must be between 10 and 500 characters")
        ])
    submit = SubmitField('Submit')


class GenreForm(FlaskForm):
    """Form to create a genre."""
    name = StringField('Genre Name',
        validators=[
            DataRequired(),
            Length(min=3, max=80, message="Genre name must be between 3 and 80 characters")
        ])
    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    """Form to create a user."""
    username = StringField('Username',
        validators=[
            DataRequired(),
            Length(min=3, max=80, message="Username must be between 3 and 80 characters")
        ])
    favorite_books = QuerySelectMultipleField('Favortie Books',
        query_factory=lambda: Book.query)
    submit = SubmitField('Submit')