from django.urls import include, path
from .views import MovieViewSet,MovieView, PostFilmView,PutFilmView,DeleteFilmView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('movies/', MovieViewSet.as_view(),name='movielist'),
    path('movies/<int:film_id>/', MovieView.as_view()),
    path('movies/<int:movie_id>', PutFilmView.as_view()),
    path('film/', PostFilmView.as_view()),
    path('deletefilm/<int:moviefilm_id>',DeleteFilmView.as_view())
    
]
if settings.DEBUG:
     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)