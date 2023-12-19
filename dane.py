users_list: list = [
    {"city":"Zamość","name":"Szymon","nick":"Spec","posts":533},
    {"city":"Warszawa","name":"Mateusz","nick":"Swietlik","posts":123},
    {"city":"Lublin","name":"Piotr","nick":"Muł","posts":231},
    {"city":"Radom","name":"Stas","nick":"Starzec","posts":1},
    {"city":"Węgorzewo","name":"Kasia","nick":"Malina","posts":34},
    {"city":"Dęblin","name":"Maja","nick":"Kalina","posts":23},
    {"city":"Toruń","name":"Oli","nick":"Olinek","posts":42},
    {"city":"Warszawa","name":"Maciej","nick":"Kamienna_twarz","posts":51},
    {"city":"Gdańsk","name":"Agatka","nick":"Agacia","posts":55001},
    {"city":"Zamość","name":"Szymon","nick":"Specialist","posts":666},
]
import sqlalchemy
class User():

    __tablename__='my_table'
    id= sqlalchemy.Column(sqlalchemy.Integer(),primary_key=True)
    city= sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    name= sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    nick= sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    posts= sqlalchemy.Column(sqlalchemy.Integer(), nullable=False)