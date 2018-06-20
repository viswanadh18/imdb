
"""
Creating the urls.py file for each app is the best way to make your application reusable by other projects.
We have to include the URL patterns of our movinfo application into the manin
URL patterns of the project. Edit the urls.py file in the app directory of current project. and make the
changes in the below code.
"""
from django.conf.urls import include, url
from movies.movinfo import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movinfo', views.api_view())

urlpatterns = [
    url('', include(router.urls)),
    url(r'^all_movies/', views.list_movies),
    url(r'^test/', views.test),
    url(r'^search/', views.sample_search),
    url(r'^add$', views.addMovies),
]