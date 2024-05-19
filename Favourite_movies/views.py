from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Genre, Director, Movie


# Create your views here.

def index(request):
    return render(request, "index.html", {
        "movies": Movie.objects.all(),
        "genres": Genre.objects.all(),
        "directors": Director.objects.all()
    })
    
def movie(request, movie_id):
    m = Movie.objects.get(id=movie_id)
    embed_url = False
    if m.trailer:
        if 'v=' in m.trailer:
            embed_url = 'https://www.youtube.com/embed/' + m.trailer.split('v=')[1]
            
    return render(request, "movie.html", {
        "movie": m,
        "embed_url": embed_url,
        "genres": m.genres.all(),
        "all_genres": Genre.objects.all(),
        "all_directors": Director.objects.all(),
    })
    
def add_movie(request):
    if request.method == 'POST':
        movie_name = request.POST.get('movie')
        img = request.FILES.get('img') 
        print('gggggggg', img)
        year = int(request.POST.get('year'))
        director_id = request.POST.get('director')
        
        director= Director.objects.get(id=director_id)
        genres = request.POST.getlist('genre')
        
        Movie.objects.create(name=movie_name, director = director, year = year, poster= img)
        movie = Movie.objects.get(name=movie_name)
        
        for g in genres:
            genre = Genre.objects.get(id=g)
            movie.genres.add(genre)
        
        return HttpResponseRedirect(reverse("index"))
    
def delete_movie(request, movie_id):
    if request.method == 'POST':
        m = Movie.objects.get(id=movie_id)
        
        m.delete()
    
        return HttpResponseRedirect(reverse("index"))
    
def edit_movie(request, movie_id):
    if request.method == 'POST':
        m = Movie.objects.get(id=movie_id)
        
        movie_name = request.POST.get('movie')
        director_id = request.POST.get('director')
        year = int(request.POST.get('year'))
        
        director= Director.objects.get(id=director_id)
        
        m.name = movie_name
        m.year = year
        m.director = director
                
        genres = request.POST.getlist('genre')
        
        for g in genres:
            genre = Genre.objects.get(id=g)
            m.genres.add(genre)
            
        m.save()
                    
        return HttpResponseRedirect(reverse("movie", args=[movie_id]))
    
   

def genres(request):
    return render(request, "genres.html", {
        "genres": Genre.objects.all()
    })

def genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    movies = genre.movies.all().order_by('year')
    return render(request, "genre.html", {
        "genre": genre,
        "movies": movies
    })
         
def add_genre(request):
    if request.method == 'POST':
        genre = request.POST.get('genre')
        Genre.objects.create(name=genre)
        
        return HttpResponseRedirect(reverse("genres"))
    
def directors(request):

    return render(request, "directors.html", {
        "directors": Director.objects.all().order_by('name')
    })

def director(request, director_id):
    director = Director.objects.get(id=director_id)
    movies = director.movies.all().order_by('year')
    return render(request, "director.html", {
        "director": director,
        "movies": movies
    })
          
def add_director(request):
    if request.method == 'POST':
        director = request.POST.get('director')
        Director.objects.create(name=director)
        
        return HttpResponseRedirect(reverse("directors"))
        
def year(request, year):
    movies = Movie.objects.filter(year=year)
    return render(request, "year.html", {
        "movies": movies,
        "year": year
    })