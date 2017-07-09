import requests


def getFavoriteMovies(URL = 'https://api.themoviedb.org/3/discover/movie?api_key=63deb316427624bb95cf1d828e19b7a2&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'):
	# Call the api from the provided url
	response = requests.get(URL)
	return response.json()['results']

def getDefaultFavoritesURL():
	# Construct the favorite movie API URL
	return getBaseApiURL() + '/movie?api_key=' + getApiKey() + '&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'

def getBaseApiURL():
	# Get the base API url for themoviedb
	return 'https://api.themoviedb.org/3'

def getApiKey():
	# This is the user api key in order to use the api
	return '63deb316427624bb95cf1d828e19b7a2'

def getYoutubeTrailerKey(movieID):
	# Construct the API URL for fetching the movie trailer and return trailer key
 	trailerURL = getBaseApiURL() + '/movie/' + str(movieID) + '/videos?api_key='+ getApiKey() + '&language=en-US'
	response = requests.get(trailerURL)
	return response.json()['results'][0]['key']
