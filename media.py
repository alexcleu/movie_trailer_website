""" the module is used to create the class Movie"""

class Movie():
    """Instaneous class for Movies and its attribute"""
    def __init__(self, title, story, poster_image, movie_trailer,rating, director):
        """Instaneous object for movie
        Args: 
          title: the movie title
          story: story of the movie
          poster_image: image url of the movie
          movie_trailer: youtube url link of the trailer
          rating: Alex's rating: out of 5 stars
          director: Director of the movie
        """
        self.title = title
        self.director = director
        self.story = story
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer
        self.rating = rating
    
