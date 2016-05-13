import webbrowser


# class for giving attributes to each Movie object
class Movie():
    """ ... this is the class documentation docstring ...
    this class offers the attributes movie title, movie release,
    storyline, poster image, and a link to the the trailer on
    youtube.
    """
    def __init__(
                self, movie_title, movie_release_date, movie_storyline,
                poster_image,
                trailer_youtube):
        """ ... this is the constructor method docstring ...
        this function creates space to add all the arguments to the
        variables for the class Movie
        """
        self.title = movie_title
        self.release_date = movie_release_date
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ ... this is the show_trailer method ...
        this function can be used to show the trailer of the Movie
        object if invoked
        """
        webbrowser.open(self.trailer_youtube_url)
