from tabulate import tabulate
from db.models import Director, Movie

# ─────────────────────────────────────────────────────
# ✅ Utility Functions
# ─────────────────────────────────────────────────────

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# ─────────────────────────────────────────────────────
# ✅ Display Functions
# ─────────────────────────────────────────────────────

def print_directors(directors):
    if not directors:
        print("No directors found.")
        return
    table = [[d.id, d.name, d.birthdate] for d in directors]
    print(tabulate(table, headers=["ID", "Name", "Birthdate"], tablefmt="fancy_grid"))

def print_movies(movies):
    if not movies:
        print("No movies found.")
        return
    table = [[m.id, m.title, m.release_year, m.genre, m.director.name] for m in movies]
    print(tabulate(table, headers=["ID", "Title", "Year", "Genre", "Director"], tablefmt="fancy_grid"))

# ─────────────────────────────────────────────────────
# ✅ Movie Functions
# ─────────────────────────────────────────────────────

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

    if director:
        movie = Movie(title=title, release_year=release_year, genre=genre, director=director)
        session.add(movie)
        session.commit()
        print(f"\n✅ Movie '{title}' added successfully!")
    else:
        print("❌ Director not found. Movie not added.")
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

# Add your other CLI helper functions here as needed
