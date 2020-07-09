from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm


class ReviewForm(FlaskForm):

    title = StringField('Review title', validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')

   
