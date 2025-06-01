from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Director, Movie
from datetime import date

engine = create_engine('sqlite:///movies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data (optional)
session.query(Movie).delete()
session.query(Director).delete()

# Add directors
spielberg = Director(name="Steven Spielberg", birthdate=date(1946, 12, 18))
nolan = Director(name="Christopher Nolan", birthdate=date(1970, 7, 30))
kubrick = Director(name="Stanley Kubrick", birthdate=date(1928, 7, 26))
scorsese = Director(name="Martin Scorsese", birthdate=date(1942, 11, 17))
bigelow = Director(name="Kathryn Bigelow", birthdate=date(1951, 11, 27))

session.add_all([spielberg, nolan, kubrick, scorsese, bigelow])
session.commit()

# Add movies
movies = [
    Movie(title="Jurassic Park", release_year=1993, genre="Adventure", director=spielberg),
    Movie(title="Schindler's List", release_year=1993, genre="Drama", director=spielberg),
    Movie(title="Inception", release_year=2010, genre="Sci-Fi", director=nolan),
    Movie(title="Interstellar", release_year=2014, genre="Sci-Fi", director=nolan),
    Movie(title="The Shining", release_year=1980, genre="Horror", director=kubrick),
    Movie(title="2001: A Space Odyssey", release_year=1968, genre="Sci-Fi", director=kubrick),
    Movie(title="Goodfellas", release_year=1990, genre="Crime", director=scorsese),
    Movie(title="The Departed", release_year=2006, genre="Crime", director=scorsese),
    Movie(title="The Hurt Locker", release_year=2008, genre="War", director=bigelow),
    Movie(title="Zero Dark Thirty", release_year=2012, genre="War", director=bigelow)
]

session.add_all(movies)
session.commit()

print("Database seeded successfully!")
