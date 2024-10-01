# app.py

from flask import Flask, jsonify, request, render_template
from model import movies, get_all_movies, add_movie, rent_movie

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movies', methods=['GET'])
def list_movies():
    """List all available movies."""
    return jsonify([{'id': movie.id, 'title': movie.title, 'genre': movie.genre, 'is_rented': movie.is_rented} for movie in get_all_movies()])

@app.route('/movies', methods=['POST'])
def create_movie():
    """Add a new movie."""
    data = request.get_json()
    title = data.get('title')
    genre = data.get('genre')

    if not title or not genre:
        return jsonify({'error': 'Title and genre are required.'}), 400

    add_movie(title, genre)
    return jsonify({'message': 'Movie added successfully!'}), 201

@app.route('/movies/<int:movie_id>/rent', methods=['POST'])
def rent_a_movie(movie_id):
    """Rent a movie by ID."""
    if rent_movie(movie_id):
        return jsonify({'message': 'Movie rented successfully!'}), 200
    return jsonify({'error': 'Movie not available for rent.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
