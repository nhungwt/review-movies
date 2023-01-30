from django.shortcuts import render
from .models import Movie

# Create your views here.
def listMovie(request):
    movies = Movie.objects.all()
    return render(request, 'listMovie.htm', {'movies':movies})

def movieDetail(request):
    pass