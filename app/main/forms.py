
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself',validators=[DataRequired()])
    submit =SubmitField('Submit')


class PostForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    blog =TextAreaField('Write your blog',validators=[DataRequired()])
    submit=SubmitField('Submit')   

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')
            