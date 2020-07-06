from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm


class ReviewForm(FlaskForm):

    title = StringField('', validators=[Required()])
    review = TextAreaField('', validators=[Required()])
    submit = SubmitField('Submit')
