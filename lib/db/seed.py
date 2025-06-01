from lib.db.models import Base, Director, Movie, Studio  # 👈 absolute import works when running directly

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date


engine = create_engine('sqlite:///lib/db/movies.db')
Session = sessionmaker(bind=engine)
session = Session()

# ───────────────────────────────────────
# ✅ Create tables if they don’t exist
# ───────────────────────────────────────
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# ───────────────────────────────────────
# ✅ Clear existing data
# ───────────────────────────────────────
session.query(Movie).delete()
session.query(Director).delete()
session.query(Studio).delete()

# ───────────────────────────────────────
# ✅ Add studios
# ───────────────────────────────────────
paramount = Studio(name="Paramount Pictures", location="Los Angeles")
warner = Studio(name="Warner Bros.", location="Burbank")
universal = Studio(name="Universal Pictures", location="Universal City")
fox = Studio(name="20th Century Studios", location="Century City")

session.add_all([paramount, warner, universal, fox])
session.commit()

# ───────────────────────────────────────
# ✅ Add directors
# ───────────────────────────────────────
spielberg = Director(name="Steven Spielberg", birthdate=date(1946, 12, 18))
nolan = Director(name="Christopher Nolan", birthdate=date(1970, 7, 30))
kubrick = Director(name="Stanley Kubrick", birthdate=date(1928, 7, 26))
scorsese = Director(name="Martin Scorsese", birthdate=date(1942, 11, 17))
bigelow = Director(name="Kathryn Bigelow", birthdate=date(1951, 11, 27))

session.add_all([spielberg, nolan, kubrick, scorsese, bigelow])
session.commit()

# ───────────────────────────────────────
# ✅ Add movies
# ───────────────────────────────────────
movies = [
    Movie(title="Jurassic Park", release_year=1993, genre="Adventure", director=spielberg, studio=universal),
    Movie(title="Schindler's List", release_year=1993, genre="Drama", director=spielberg, studio=universal),
    Movie(title="Inception", release_year=2010, genre="Sci-Fi", director=nolan, studio=warner),
    Movie(title="Interstellar", release_year=2014, genre="Sci-Fi", director=nolan, studio=paramount),
    Movie(title="The Shining", release_year=1980, genre="Horror", director=kubrick, studio=warner),
    Movie(title="2001: A Space Odyssey", release_year=1968, genre="Sci-Fi", director=kubrick, studio=fox),
    Movie(title="Goodfellas", release_year=1990, genre="Crime", director=scorsese, studio=warner),
    Movie(title="The Departed", release_year=2006, genre="Crime", director=scorsese, studio=warner),
    Movie(title="The Hurt Locker", release_year=2008, genre="War", director=bigelow, studio=fox),
    Movie(title="Zero Dark Thirty", release_year=2012, genre="War", director=bigelow, studio=universal)
]

session.add_all(movies)
session.commit()

print("✅ Database seeded successfully!")
