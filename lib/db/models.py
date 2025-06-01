from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birthdate = Column(Date)

    movies = relationship('Movie', back_populates='director')

    def __repr__(self):
        return f"<Director(id={self.id}, name='{self.name}', birthdate={self.birthdate})>"

class Studio(Base):
    __tablename__ = 'studios'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)

    movies = relationship('Movie', back_populates='studio')

    def __repr__(self):
        return f"<Studio(id={self.id}, name='{self.name}', location='{self.location}')>"

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    release_year = Column(Integer)
    director_id = Column(Integer, ForeignKey('directors.id'))
    studio_id = Column(Integer, ForeignKey('studios.id'))

    director = relationship('Director', back_populates='movies')
    studio = relationship('Studio', back_populates='movies')

    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}', year={self.release_year})>"
