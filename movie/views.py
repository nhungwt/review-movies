from django.shortcuts import render
from .models import Movie

# Create your views here.
def listMovie(request):
    movies = Movie.objects.all()
    return render(request, 'listMovie.htm', {'movies':movies})

def movieDetail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movie_detail.htm', {'movie':movie})