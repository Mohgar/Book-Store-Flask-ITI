from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, NumberRange
from datetime import datetime


class AddBookForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    Publish_date = DateTimeField(
        "Publish Date",
        validators=[DataRequired()],
        format="%Y-%m-%d %H:%M:%S",
        default=datetime.utcnow(),
    )
    price = IntegerField(
        "Price",
        validators=[
            DataRequired(),
            NumberRange(min=0, message="Price must be a positive number."),
        ],
    )
    author_name = StringField("Author Name", validators=[DataRequired()])
    image = StringField("Image", validators=[DataRequired()])
    added_at = DateTimeField(
        "Added at",
        validators=[DataRequired()],
        format="%Y-%m-%d %H:%M:%S",
        default=datetime.utcnow(),
    )
    appropriate_age = IntegerField(
        "Appropriate Age",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=120, message="Age must be between 0 and 120."),
        ],
    )
    submit = SubmitField("Submit")



