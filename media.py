import webbrowser


class Movie():
    """ This provides a way to store movie related information"""

    RATINGS = ["PG-13", "PG", "R", "G", "NC-17"]
    RANKING_SCORE = [1, 2, 3, 4, 5]
    CATEGORY = ["comedy", "adventure", "romance", "thriller"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_url, synopsis, release_year):
        """
        A movie object consists of a title, story line, url to the poster img,
        url to the youtube trailer, synopsis and a release year. It could be
        expanded if needed based on future requirements
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url
        self.synopsis = synopsis
        self.release_year = release_year

    def show_trailer(self):
        # to opens the youtube trailer video using the url instance of the obj
        webbrowser.open(self.trailer_youtube_url)
