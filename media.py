""" the module is used to create the class Movie"""

class Movie():
 """this class is to generate instance for movies and its attribute"""
    def __init__(self, title, story, poster_image, movie_trailer):
    
     """Instaneous object for movie
       
        Args: 
         title: the movie title
         story: story of the movie
         poster_image: image url of the movie
         movie_trailer: youtube url link of the trailer
    """
        self.title = title
        self.story = story
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer