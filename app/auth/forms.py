from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo
from .. models import User


class RegistrationForm(FlaskForm):
    email =StringField('Your email address',validators=[DataRequired(),Email()])
    username =StringField('Enter your username',validators=[DataRequired()])
    password =PasswordField('Password',validators=[DataRequired(),EqualTo('password_confirm',message='password must match')])
    submit =SubmitField('Sign Up')


    def valid_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username =data_field.data).first():
            raise ValidationError('That username is taken')         

