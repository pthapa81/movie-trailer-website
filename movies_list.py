from movie_services import movies
import media
import json
import fresh_tomatoes
"""
List of methods and helper methods.
These methods use movies service defined in move_services directory
Used to construct favorite movie object list and full Urls for videos and poster
"""
def generate_favorite_movies():
  # Calls method from movies service to generate list of favorite movies
  favMovies = movies.getFavoriteMovies()
  movieObjList = getMovieObjList(favMovies)
  return movieObjList

def getMovieObjList(favoriteMovies):
  # helper method to construct a list out of the json response
  movieObjList = []
  for movie in favoriteMovies:
    movieObjList.append(constructMovieObj(movie))
  return movieObjList

def constructMovieObj(favoriteMovie):
  # helper method to construct a movie object
  title = favoriteMovie['title']
  storyline = favoriteMovie['overview']
  poster_image = getFullPosterImageUrl(favoriteMovie['poster_path'])
  trailer_url = getTrailerUrl(favoriteMovie['id'])
  synopsis = favoriteMovie['overview']
  release_year = favoriteMovie['release_date']
  movieObj = media.Movie(title, storyline, poster_image,
                         trailer_url, synopsis, release_year)
  return movieObj

def getFullPosterImageUrl(partialUrl):
  # helper method to construct full poster url from the url in the response
  fullPosterUrl = "http://image.tmdb.org/t/p/w185/" + partialUrl
  return fullPosterUrl

def getTrailerUrl(movieID):
  # helper method to construct full youtube url from the url in the response
  fullPosterUrl = "https://www.youtube.com/watch?v=" + movies.getYoutubeTrailerKey(movieID)
  return fullPosterUrl
