from django.db import models
from django.contrib.auth.models import User
from django.db import models



# Create your models here.

class Movies(models.Model):
    popularity = models.CharField(max_length=50, null=True)
    director = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=50, null=True)
    imdb_score = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    dt_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dt_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
"""
In our basic model for imdb movie posts. we defined some fields.
1) Popularity: It tells the rating of the movie.
2) director: name of the movie director
3) genre: It shows the category of the movie. Like, Art, Music, Literature or Action.
4)imdb_score: User rating given by the user. The user gives the rating by choosing producer, director or actor.
5)dt_added: It tells when the post was published
6)dt_updated: It indicates the last time the post has been updated.  
"""
class Meta:
    ordering = ('-dt_added',)

# The use of the ordering field is to display the records in descending order

    def __str__(self):
        return self.ordering

"""_str__(): method is the default human -readble representation of
  of the object. Django will use it in many places."""

"""
For migrations part, Actually, I am mysql database for accessing the data. Once migrations applied. It creates the data 
model with the above field names.

"""
