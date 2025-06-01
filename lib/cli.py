from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime  # ✅ Added for date conversion
from db.models import Director, Movie
from helpers import (
    print_directors,
    print_movies,
    get_valid_int,
    add_movie,
    delete_movie
)

engine = create_engine('sqlite:///lib/db/movies.db')
Session = sessionmaker(bind=engine)
session = Session()

def main():
    while True:
        print("\n🎬 Movie Database CLI 🎬")
        print("1. Manage Directors")
        print("2. Manage Movies")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            director_menu()
        elif choice == '2':
            movie_menu()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1–3.")

def director_menu():
    while True:
        print("\n📁 Director Menu")
        print("1. View All Directors")
        print("2. Add New Director")
        print("3. Find Director by ID")
        print("4. Delete Director")
        print("5. View Movies by Director")
        print("6. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            directors = session.query(Director).all()
            print_directors(directors)

        elif choice == '2':
            name = input("Enter director name: ").strip()
            birth_str = input("Enter birthdate (YYYY-MM-DD): ").strip()
            try:
                birth = datetime.strptime(birth_str, "%Y-%m-%d").date()
                director = Director(name=name, birthdate=birth)
                session.add(director)
                session.commit()
                print(f"✅ Director '{name}' added.")
            except ValueError:
                print("❌ Invalid date format. Please use YYYY-MM-DD.")
            except Exception as e:
                print("❌ Error adding director:", e)
                session.rollback()

        elif choice == '3':
            id = get_valid_int("Enter director ID: ")
            director = session.get(Director, id)
            if director:
                print(director)
            else:
                print("Director not found.")

        elif choice == '4':
            id = get_valid_int("Enter director ID to delete: ")
            director = session.get(Director, id)
            if director:
                session.delete(director)
                session.commit()
                print("Director deleted.")
            else:
                print("Director not found.")

        elif choice == '5':
            id = get_valid_int("Enter director ID: ")
            director = session.get(Director, id)
            if director:
                print_movies(director.movies)
            else:
                print("Director not found.")

        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select 1–6.")

def movie_menu():
    while True:
        print("\n🎞️ Movie Menu")
        print("1. View All Movies")
        print("2. Add New Movie")
        print("3. Find Movie by ID")
        print("4. Delete Movie")
        print("5. Search Movies by Genre")
        print("6. Search Movies by Year")
        print("7. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            movies = session.query(Movie).all()
            print_movies(movies)

        elif choice == '2':
            add_movie(session)

        elif choice == '3':
            id = get_valid_int("Enter movie ID: ")
            movie = session.get(Movie, id)
            if movie:
                print(movie)
            else:
                print("Movie not found.")

        elif choice == '4':
            delete_movie(session)

        elif choice == '5':
            genre = input("Enter genre to search: ").strip()
            movies = session.query(Movie).filter(Movie.genre.ilike(f"%{genre}%")).all()
            print_movies(movies)

        elif choice == '6':
            year = get_valid_int("Enter release year: ")
            movies = session.query(Movie).filter_by(release_year=year).all()
            print_movies(movies)

        elif choice == '7':
            break
        else:
            print("Invalid choice. Please select 1–7.")

if __name__ == '__main__':
    main()
