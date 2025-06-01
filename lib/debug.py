import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Director, Movie

engine = create_engine('sqlite:///lib/db/movies.db')
Session = sessionmaker(bind=engine)
session = Session()

ipdb.set_trace()
