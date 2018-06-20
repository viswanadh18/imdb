from django.shortcuts import render
from django.shortcuts import get_object_or_404
from movies.movinfo.models import Movies
from movies.movinfo.serializers import MoviesListSeralizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from movies.movinfo.serializers import UserSerializer, GroupSerializer

""" In the above modules get_object_or_404() shortcut to retrieve
    the desired article. This function retrieve the object that matches with given parameters
    or it returns an HTTP404(Not Found) exception is found.
    Finally, render() is used for render the movies using a template. 
"""

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_added')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# ----------------------------
# Create your views here.

"""
get() method, we have accessed this method using Movies.objects.all(). 
Each django model has at least one manager and the default manager is called objects
you get a QuerySet object by using models manager. To retrieve all objects from a table, just using the all() method
on the default manager.
For retrieving objects in django. It works on the Object- relational mapping(ORM).
It is based on the Query Set. A QuerySet is a collection of objects from our database to limit the result.  
filter() method can be used for retrieve all articles published in the year 2018 by using the QuerySet.
Ex: Movies.objects.filter(article_post_year=2018)

QuerySet are evaluated in the following cases:
-> The first time you create over them
-> When slice them. for instance: Movies.objects.all()[:4]
-> When you pickle them
-> When you call repr() or len() on them
-> When you explicitly call list() method on them
-> when you test it in a statement such as bool(), and, or. 
"""
@api_view(['GET'])
def test(request):
    return Response({'Everything': 'Fair and Lovely', 'Welcome': 'everybody'})


@api_view(['GET'])
def list_movies(request):
    if request.method == 'GET':
        movies = Movies.objects.all()
        serializer = MoviesListSeralizer(movies, many=True)
        return Response(serializer.data)
    # return Response(movies.values())


@api_view(['GET'])
def sample_search(request):
    field = request.GET.get("field", "name")
    search_str: object = request.GET.get("str")
    print(field, search_str)
    if field == "name":
        movies = Movies.objects.filter(name__contains=search_str)
        serializer = MoviesListSeralizer(movies, many=True)
        return Response(serializer.data)
    else:
        return Response({"error": "name not found"})


@api_view(['POST'])
def addMovies(request):
    name = request.POST.get("name", None)
    popularity = request.POST.get("popularity", None)
    imdb_score = request.POST.get("imdb_score", None)
    movies = Movies.objects.create(name=name, popularity=popularity, imdb_score=imdb_score)

    return Response({'message': 'movies {:d} created'.format(movies.id)}, status=301)
