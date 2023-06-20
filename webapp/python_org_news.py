from datetime import datetime
import requests
from bs4 import BeautifulSoup

from webapp.model import db, News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False
    
def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').find_all('li')
        # all_news = all_news.find_all('li')
        result_news = []
        for news in all_news:  #пробежались по списку нашли 'a' дальщше text и вывели
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)
    #         result_news.append({
    #             'title': title,
    #             'url' : url,
    #             'published' : published
    #         })  #после
    #     return result_news
    # return False

def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()
 
 
 
 
 
 
            # print(title)  до
            # print(url)
            # print(published)

    # print(all_news)

# if __name__ == "__main__":
    # html = get_html("https://www.python.org/blogs/")
    # if html:
    #    news = get_python_news(html)
    #    print(news)
       
       
        # with open("python.org.html", "w", encoding="utf8") as f:
        #     f.write(html)