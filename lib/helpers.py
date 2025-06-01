from tabulate import tabulate
from db.models import Director, Movie, Studio

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def print_directors(directors):
    if not directors:
        print("No directors found.")
        return
    table = [[d.id, d.name, d.birthdate] for d in directors]
    print(tabulate(table, headers=["ID", "Name", "Birthdate"], tablefmt="fancy_grid"))

def print_studios(studios):
    if not studios:
        print("No studios found.")
        return
    table = [[s.id, s.name, s.location] for s in studios]
    print(tabulate(table, headers=["ID", "Name", "Location"], tablefmt="fancy_grid"))

def print_movies(movies):
    if not movies:
        print("No movies found.")
        return
    table = [[m.id, m.title, m.release_year, m.genre, m.director.name, m.studio.name] for m in movies]
    print(tabulate(table, headers=["ID", "Title", "Year", "Genre", "Director", "Studio"], tablefmt="fancy_grid"))

def add_studio(session):
    print("\n🏢 Add New Studio")
    name = input("Enter studio name: ").strip()
    location = input("Enter studio location: ").strip()

    studio = Studio(name=name, location=location)
    session.add(studio)
    session.commit()
    print(f"\n✅ Studio '{name}' added successfully!")

def add_movie(session):
    print("\n🎞️ Add New Movie")

    title = input("Enter movie title: ")
    release_year = get_valid_int("Enter release year: ")
    genre = input("Enter genre: ")

    print("\n🎬 Available Directors:")
    directors = session.query(Director).all()
    if not directors:
        print("No directors found. Please add a director first.")
        return
    print_directors(directors)
    director_id = get_valid_int("Enter director ID from the list above: ")
    director = session.query(Director).filter_by(id=director_id).first()

    print("\n🏢 Available Studios:")
    studios = session.query(Studio).all()
    if not studios:
        print("No studios found. Please add a studio first.")
        return
    print_studios(studios)
    studio_id = get_valid_int("Enter studio ID from the list above: ")
    studio = session.query(Studio).filter_by(id=studio_id).first()

    if director and studio:
        movie = Movie(title=title, release_year=release_year, genre=genre,
                      director=director, studio=studio)
        session.add(movie)
        session.commit()
        print(f"\n✅ Movie '{title}' added successfully!")
    else:
        print("❌ Director or Studio not found. Movie not added.")

def delete_movie(session):
    print("\n❌ Delete Movie")

    movies = session.query(Movie).all()
    if not movies:
        print("No movies found.")
        return

    print("\n🎬 Available Movies:")
    print_movies(movies)

    movie_id = get_valid_int("Enter movie ID to delete: ")
    movie = session.query(Movie).filter_by(id=movie_id).first()

    if movie:
        confirm = input(f"Are you sure you want to delete '{movie.title}'? (y/n): ").strip().lower()
        if confirm == 'y':
            session.delete(movie)
            session.commit()
            print(f"\n✅ Movie '{movie.title}' deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("❌ Movie not found.")
