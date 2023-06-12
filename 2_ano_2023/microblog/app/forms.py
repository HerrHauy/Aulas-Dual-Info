from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User
from wtforms import TextAreaField
from wtforms.validators import Length

class LoginForm(FlaskForm):
	username = StringField('Nome de usuário', validators=[DataRequired()])
	password = PasswordField('Senha', validators=[DataRequired()])
	remember_me = BooleanField('Continuar logado')
	submit = SubmitField('Logar')


class RegistrationForm(FlaskForm):
	username = StringField('Nome de usuário', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Senha', validators=[DataRequired()])
	password2 = PasswordField('Repita a senha', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Registrar')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Esse nome já foi usado. Seja mais criativo, palhaço.')


	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Esse email já foi usado. Não me provoca!')



class EditProfileForm(FlaskForm):
	username = StringField('Nome de usuário', validators=[DataRequired()])
	about_me = TextAreaField('Conte um pouco sobre você!:', validators=[Length(min=0,max=140)])
	submit = SubmitField('Enviar')