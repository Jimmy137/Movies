from django.urls import path
from . import views
from django.conf.urls.static import static  
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import cache_control

urlpatterns = [
    path("movies", views.index, name="index"),
    path("genres", views.genres, name="genres"),
    path("directors", views.directors, name="directors"),
    path("movies/<int:movie_id>", views.movie, name="movie"),
    path("movies/<int:movie_id>/edit", views.edit_movie, name="edit_movie"),
    path("delete_movie/<int:movie_id>", views.delete_movie, name="delete_movie"),
    path("add_movie", views.add_movie, name="add_movie"),
    path("genres/<int:genre_id>", views.genre, name="genre"),
    path("add_genre", views.add_genre, name="add_genre"),
    path("directors/<int:director_id>", views.director, name="director"),
    path("add_director", views.add_director, name="add_director"),
    path("movie/<int:year>", views.year, name="year"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))