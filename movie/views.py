from django.shortcuts import render

# Create your views here.
def listMovie(request):
    return render(request, 'listMovie.htm')