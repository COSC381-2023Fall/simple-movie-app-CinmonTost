# Import the Movies class from movies.py
from movies import Movies

# Initialize the Movies object
movies = Movies(r'C:\Users\shaun\Desktop\COSC381\simple-movie-app-CinmonTost\backend\movies.txt')

# Lists all movie names
def list_movie_names():
    movie_names = [movie['name'] for movie in movies._movies]
    return ', '.join(movie_names)

# Search movies by name
def search_movies_by_name(keyword):
    result = [movie['name'] for movie in movies._movies if keyword.lower() in movie['name'].lower()]
    return ', '.join(result)

# Search movies by cast
def search_movies_by_cast(keyword):
    results = []
    for movie in movies._movies:
        movie_name = movie['name']
        cast = [actor for actor in movie['cast'] if keyword.lower() in actor.lower()]
        if cast:
            results.append(f'{movie_name}\n{cast}')
    return results

def searchMovieId(movie_id):
    return movies._movies[movie_id]

def replaceMovie(movie_id, new_movie): 
    movies._movies[movie_id] = new_movie
    return movies._movies[movie_id]

def deleteMovie(movie_id):
    movieD = searchMovieId(movie_id)
    movies._[movie_id] = None
    return movieD

def addMovie(movie_data):
    movie_data["movie_id"] = len(movies._movies) + 1
    movies._movies.append(movie_data)
    return searchMovieId((len(movies._movies)))