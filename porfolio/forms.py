from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Email,ValidationError

class AddCourseForm(FlaskForm):
    name = StringField('Course Name',validators=[DataRequired()])
    author_id = StringField('Doctor Full Name',validators=[DataRequired()])
    submit = SubmitField('Add Course')
