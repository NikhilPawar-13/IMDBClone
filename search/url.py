from django.contrib import admin

from django.urls import path, include

from . import views



urlpatterns = [

    path('', views.query_search, name="query_search_imdb"),
    path('watchTrailer/',views.getYTtrailer, name = "getYTtrailer")

]