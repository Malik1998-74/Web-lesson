from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField   # типы полей кнопку (поможет создать строку и строку для ввода поролей и кнопочку)
from wtforms.validators import DataRequired # помогает избежать ручных проверок 

class LoginForm(FlaskForm): # создаем LoginFrom который наследует FlaskFrom
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"}) # поле имя первый параметр то что хотим написать возле поля(имя пользователя) и список валидаторов класс который помогает нам избежать ручных проверок(то что в поле есть введеные данные)
    password = PasswordField('Пороль', validators=[DataRequired()], render_kw={"class": "form-control"})  # тоже самое 
    submit = SubmitField('Отправить!', render_kw={'class': 'btn btn-primary'})  # тоже самое





