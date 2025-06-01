from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birthdate = Column(Date)

    movies = relationship("Movie", back_populates="director", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Director {self.id}: {self.name} ({self.birthdate})>"

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_year = Column(Integer)
    genre = Column(String)
    director_id = Column(Integer, ForeignKey('directors.id'))

    director = relationship("Director", back_populates="movies")

    def __repr__(self):
        return f"<Movie {self.id}: '{self.title}' ({self.release_year}, {self.genre})>"
