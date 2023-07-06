from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User


app = create_app()

with app.app_context():
    username = input('Ввидите имя: ')  # запрашиваем имя пользователя

    if User.query.filter(User.username == username).count():
        print('Пользователь с таким иминем существует')  # проверяем есть ли уже такой пользователь
        sys.exit(0)

    password1 = getpass('Введите пороль')   # спрашиваем 2 раза при помощи getpass пороль
    password2 = getpass('Повторите пороль')  # проверяем что он одинаковый 

    if not password1 == password2:
        print('Пороли не одинаковые')
        sys.exit(0)

    new_user = User(username=username, role='admin')  # создаем пользователя
    new_user.set_password(password1)  # ставим ему пороль(пороль превращаеться в шифрованную строку(hash))

    db.session.add(new_user)  # тут добовляем 
    db.session.commit()  
    print('Создан пользователь с id={}'.format(new_user.id))