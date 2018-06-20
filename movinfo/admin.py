from django.contrib import admin
from .models import Movies

# Register your models here.

"""
In this admin.py file. we create a simple administration site to manage the articles.
Django comes with a built in administration interface this is very useful for editing content.
In this file, Configuring how you want your models to displayed in admin page.
Here I am created three different fields. 
1) list_display: It allows you to set the fields of model.
2) search_fields: It provides the search filed for searching the article
3) list_filter: It used for to filter the article by using the provided fileds like
                 dt_added, dt_updated and imdb_score.   
"""

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'genre', 'imdb_score', 'popularity')
    search_fields = ('name', 'director', 'genre')
    list_filter = ('name', 'dt_added', 'dt_updated', 'imdb_score')


admin.site.register(Movies, MovieAdmin)


"""First we need to create the super user to manage the admin site
    for the following command:
 >>>python manage.py createsuperuser
 
 It asks the username, email and password.
 Ex:
    Username (leave blank to use 'admin'): admin
    Email address: admin@admin.com
    Password: ********
    Password (again): ********
    Superuser created successfully.
    ############################################
    In this Project super user created by me
    ie; Username: viswa
        Password: password123
    ############################################   
    
"""