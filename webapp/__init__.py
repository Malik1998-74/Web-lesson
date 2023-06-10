from flask import Flask, render_template

from webapp.model import db
from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)    # инициализируем нашу базу данных 


    @app.route('/')
    def index():
        title = 'Новости Python'   # короче это у нас главная страница
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])  # переменнаы погода получилось с помощью функции
        news_list = get_python_news()
        return render_template("index.html", page_title=title, weather=weather, news_list=news_list)  # выполняет рендеринг указанного шаблона и добавляет результат в ответ возвращает шаблон то что видим html название и функцию погоды

    return app
# if __name__ == "__main__":
#     app.run(debug=True)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    # if weather:
    #     weather_text = f"Погода: {weather['temp_C']}, ощущаеться как {weather['FeelsLikeC']}"  логига отображения перешла в шаблон
    # else:
    #     weather_text = "Сервес погоды временно не доступен"