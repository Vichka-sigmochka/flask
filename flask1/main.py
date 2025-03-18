from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer1.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = 'captain'
    user.speciality = "research enginner"
    user.address = 'module_1'
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    user1 = User()
    user1.surname = "Biba"
    user1.name = "Boba"
    user1.age = 10
    user1.position = 'doctor'
    user1.speciality = "enginner"
    user1.address = 'module'
    user1.email = "bibaboba@mars.org"
    db_sess.add(user1)
    user2 = User()
    user2.surname = "Pomidor"
    user2.name = "Byba"
    user2.age = 40
    user2.position = 'listener'
    user2.speciality = "cooking"
    user2.address = 'module_2'
    user2.email = "pomidorpomidor@mars.org"
    db_sess.add(user2)
    db_sess.commit()
    #app.run()


if __name__ == '__main__':
    main()