from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Movie
import json


def signup(request):
    decoded_data = request.body.decode('utf-8')
    data = json.loads(decoded_data)
    print(data)
    user = User.objects.create_user(data["name"], data["email"], data["password"])
    return HttpResponse('signed up successfully')

def signin(request):
    data = json.loads(request.body.decode('utf-8'))
    user = authenticate(username=data['username'], password=data["password"])
    if user is not None:
        return HttpResponse('logged in up successfully')
    else:
        return HttpResponse('ops not logged in')


def movie(request):
    # if request.method == "GET":
    #     all_movies = Movie.objects.all()
    #     return HttpResponse(all_movies)

    if request.method == "POST":
        if request.user.is_authenticated:
            data = json.loads(request.body.decode('utf-8'))
            m = Movie(title=data['title'], body=data['body'], rate=data['rate'])
            m.save()
            return HttpResponse('the movie posted successfully')
        else:
            return HttpResponse('ops not authenticated')