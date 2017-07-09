from movie_services import movies
import media
import json
import fresh_tomatoes

def generate_favorite_movies():
  favMovies = movies.getFavoriteMovies() 
  movieObjList = getMovieObjList(favMovies)
  return movieObjList

def getMovieObjList(favoriteMovies):
  movieObjList = []
  for movie in favoriteMovies:
    movieObjList.append(constructMovieObj(movie))
  return movieObjList  

def constructMovieObj(favoriteMovie):
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
  fullPosterUrl = "http://image.tmdb.org/t/p/w185/" + partialUrl
  return fullPosterUrl

def getTrailerUrl(movieID):
  fullPosterUrl = "https://www.youtube.com/watch?v=" + movies.getYoutubeTrailerKey(movieID)
  return fullPosterUrl

