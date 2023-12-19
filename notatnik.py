

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

class User(Base):
    __tablename__ = 'mmmmy_table'

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(), nullable=True)
    location =  sqlalchemy.Column('geom',Geometry(geometry_type='POINT', srid=4326), nullable= True)

Base.metadata.create_all(engine)



Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

### Create
lista_users: list = []
fake = Faker()

# for item in range(10_000):
#     lista_users.append(
#       User(
#         name = fake.name(),
#         location = f'POINT({random.uniform(14,24)} {random.uniform(49,55)})'
#
#     ))
# session.add_all(lista_users)
# session.commit()

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


