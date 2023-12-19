import random
import sqlalchemy
import  os
import  sqlalchemy.orm
from   dotenv import load_dotenv
from geoalchemy2 import Geometry
from faker import Faker

from dml import User

load_dotenv()

db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv("POSTGRES_USER"),
    password= os.getenv("POSTGRES_PASSWORD"),
    host= os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DB"),
    port=os.getenv("POSTGRES_PORT")
)
engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()

Base = sqlalchemy.orm.declarative_base()


Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

### Create
lista_users: list = []
fake = Faker()

for item in range(10_000):
    lista_users.append(
      User(
        name = fake.name(),
        location = f'POINT({random.uniform(14,24)} {random.uniform(49,55)})'

    ))
session.add_all(lista_users)
session.commit()

### Read and select

users_from_db = session.query(User).all()
for user in users_from_db:
    if user.name =='Janek':
        user.name == "Stachu"

#users_from_db = session.query(User),filter(User.name=="Mark Perry")
session.commit()

session.flush()
connection.close()
engine.dispose()
def main (

)


if __name__ == __main__:
    main()

