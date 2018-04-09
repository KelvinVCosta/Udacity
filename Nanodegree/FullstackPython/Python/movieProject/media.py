# This file was created following the videos from the Nanodegree
import webbrowser


class Movie():
    """ This class provides a way to store movie related information
    To implement this class do not worry about self, just pass the other 4
    atributes and all will work fine

    __init__ Parameters
        movie_title (String)
        movie_storyline (String)
        poster_image (String)
        trailer_youtube (String)

    Here is an example:
        movieName = media.Movie("Movie example",
                                "A little about how to implement it",
                                "Put a nice movie poster here",
                                "And at last, the movie trailer ")


    With all this information, you may now use the show_trailer
    Need an example?

        movieName.show_trailer()

    Now you know all about this class and its methods
    Have fun!!!

    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
