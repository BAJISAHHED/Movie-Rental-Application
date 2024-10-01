# model.py

class Movie:
    def __init__(self, id, title, genre, is_rented=False):
        self.id = id
        self.title = title
        self.genre = genre
        self.is_rented = is_rented

# In-memory storage for movies
movies = [
    Movie(1, "The Matrix", "Action"),
    Movie(2, "The Godfather", "Drama"),
    Movie(3, "Toy Story", "Animation"),
]

def get_all_movies():
    return movies

def add_movie(title, genre):
    new_id = len(movies) + 1
    new_movie = Movie(new_id, title, genre)
    movies.append(new_movie)

def rent_movie(movie_id):
    for movie in movies:
        if movie.id == movie_id and not movie.is_rented:
            movie.is_rented = True
            return True
    return False
