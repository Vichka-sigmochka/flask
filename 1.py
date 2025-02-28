from flask import Flask, url_for

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
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, арс!</title>
                  </head>
                  <body>
                  <h1>Жди нас Марс!</h1>
                  <img src="{url_for('static', filename='img/img.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""

@app.route('/promotion_image')
def return_sample_page1():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                  <h1>Жди нас Марс!</h1>
                  <img src="{url_for('static', filename='img/img.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-success" role="alert">
                    <p>Человечество вырастает из детства.</p>
                    </div>
                    <div class="alert alert-primary" role="alert">
                        Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-light" role="alert">
                    Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-primary" role="alert">
                        И начнем с Марса!
                    </div>
                    <div class="alert alert-dark" role="alert">
                      Присоединяйся!
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')