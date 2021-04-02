from django.shortcuts import render

import requests
import json
import imdb

from googleapiclient.discovery import build
from django.conf import settings

from rest_framework.response import Response
from django.http import HttpResponse, Http404

from django.shortcuts import render, redirect


# Create your views here.


def query_search(request):

    context = {}

    if request.method == 'POST':

        try:
            url = settings.RAPID_API_BASE_URL
            name = request.POST['search']
            print(request.POST['search'])
            url = url + f"?s={ request.POST['search'] }&page=1&r=json"
            print(url)

            headers = {
                'x-rapidapi-key': '35185625ffmshae485834fdadb9ap1948bajsn1bbdee7db0ae',
                'x-rapidapi-host': 'movie-database-imdb-alternative.p.rapidapi.com',
                'useQueryString': 'true',
                'Content-Type': 'application/json'
            }

            payload = json.dumps({
                "upload_date": "",
                "read": "True"
            })
            response = requests.request(
                "GET", url, headers=headers, data=payload)

            print(response.json()['Search'])
            context = {
                'movie_list': response.json()['Search']
            }
        except Exception as e:
            return render(request, 'pagenotfound.html')

    return render(request, 'search.html', context)


def getYTtrailer(request):

    imdb = request.GET.get('imdb', -1)
    title = request.GET.get('title', -1)
    context = {}
    print(type(title), title,type(imdb),imdb)    

    trailerUrl = ""
    try:             
        params = {
            'part': "snippet",
            'q': title + " official trailer",
            'key':  "AIzaSyB22y4fVC5YNq60eO83a6A3DP9WsYdf_gk"
        }

        result = requests.get(settings.YOUTUBE_API_BASE_URL, params=params)

        data = result.json()
       
        trailerUrl = settings.YOUTUBE_BASE_URL + \
            result.json()['items'][0]['id']['videoId']
    except Exception as e:
        print("Trailer does not exist")

    try:
        url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

        querystring = {"type": "get-movie-details", "imdb": imdb}

        headers = {
            'x-rapidapi-key': '35185625ffmshae485834fdadb9ap1948bajsn1bbdee7db0ae',
            'x-rapidapi-host': 'movies-tvshows-data-imdb.p.rapidapi.com',
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        print(response.json())
    
    except Exception as e:
        print("Info not found")
        return render(request, 'pagenotfound.html') 



    context = {
        'youtubeTrailer' : trailerUrl,
        'movieDetails' : response.json(),
        'title' : title
    }
   
    return render(request,'movieDetails.html',context)