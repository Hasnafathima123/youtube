from django.shortcuts import render
import requests
def index(request):
    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzNjUxODEyYmNhZGUwZmJiMmY2MzA4NTBkYjRhMzQ0ZSIsInN1YiI6IjY1NzE3YTkyN2ViNWYyMDE0ZmVhNjg3ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RY58eDhy78PGkuu4dq5wMnGOXBzUs2IFdH5wJIw8L2I"
    }
    response = requests.get(url, headers=headers)
    posts = response.json()
    data = posts['results']
    return render(request,"index.html",{"data":data})

# Create your views here.
