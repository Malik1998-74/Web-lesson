from flask import Flask, flash, render_template, redirect, url_for    # отображает щаблоны (берет шаблон) flash(позволяет передовать сообщения со страницы на страницу ) redirect(делает перенаправления стр на стр)url_for(позволяет преоброзовать по названию фунцкии получить url например фунция index а url(\))
from flask_login import LoginManager, current_user, login_required, login_user, logout_user  # login_required (это дикоратор)

from webapp.forms import LoginForm  # импортируем нашу класс из forms.py
from webapp.model import db, News, User
# from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)    # инициализируем нашу базу данных 

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):   # функция которая будет проверять и получать нужного пользователя(будет вытаскивать юсер айди и предовать в функцию load_user)
        return User.query.get(user_id)  # тут делаем запрос к базе данных(получение по id в model.py пользователя у которого id равен тому о придет если придет один будет один)


    @app.route('/')
    def index():
        title = 'Новости Python'   # короче это у нас главная страница
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])  # переменнаы погода получилось с помощью функции
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template("index.html", page_title=title, weather=weather, news_list=news_list)  # выполняет рендеринг указанного шаблона и добавляет результат в ответ возвращает шаблон то что видим html название и функцию погоды

    @app.route('/login')   # добавим роут который бутем показыать этот класс
    def login():
        if current_user.is_authenticated:  # короче если пользователь уже залогинел он не будет повторно открывать это окно а будет выбрасывать на главную стр
            return redirect(url_for('index'))
        title = 'Авторизация'   # заголовок
        login_form = LoginForm()  # создаем экземпляр формы(когда вызвали соскобочками то создался логин форм и положили в эту переменную)
        return render_template('login.html', page_title=title, form=login_form)
    
    @app.route('/process-login', methods=['POST'])  # роут который проверят данные
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user =User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)  # если пользователь вошел на сайт мы его запоминаем
                flash('Вы успешно вошли на сайт')  # что бы передать сообщение
                return redirect(url_for('index'))  # перекидываем его на главную стр
            
        flash('Неправильные имя или пороль')  # если не прошло 
        return redirect(url_for('login')) # перекидываем на стр логин

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))


    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ!'
        else:
            return 'У вас отсутствуют права администратора!'
    return app
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# if __name__ == "__main__":
#     app.run(debug=True)
  
  
  
    # if weather:
    #     weather_text = f"Погода: {weather['temp_C']}, ощущаеться как {weather['FeelsLikeC']}"  логига отображения перешла в шаблон
    # else:
    #     weather_text = "Сервес погоды временно не доступен"