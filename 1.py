from flask import Flask

app = Flask(__name__)


@app.route('/')
def title():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def index1():
    countdown_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, арс!</title>
                  </head>
                  <body>
                  <img src="{url_for('static', filename='img/img.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <h1>Вот она какая, красная планета.</h1>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')