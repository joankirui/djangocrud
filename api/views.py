from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import MovieSerializer,MovieMiniSerializer
from .models import Movie
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
from django.utils.decorators import method_decorator

class MovieViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    # def list(self, request, *args, **kwargs):
    #     movies = Movie.objects.all()
    #     serializer = MovieMiniSerializer(movies, many=True)
    #     return Response(serializer.data)
    
    
class MovieView(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self,request,*args, **kwargs):
        film_id = kwargs.get('film_id')
        film = Movie.objects.get(pk=film_id)
        serializer = MovieSerializer(film)
        return Response(serializer.data)
        
        
class PutFilmView(APIView):
    '''
    API endpoints that allows users to write
    '''
    def put(self,request,*args,**kwargs):
        '''
        Update the movie items with given film_id
        '''
        film_id = kwargs.get('movie_id')
        # film_instance = self.get_object(film_id, request.user.id)
        film_instance = Movie.objects.get(pk=film_id)
        if not film_instance:
            return Response(
                {"res": "Object with film id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'year': request.data.get('year')
        }
        serializer = MovieSerializer(instance= film_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostFilmView(generics.CreateAPIView):
    '''
    API endpoints that allows users to create new films
    '''
    def post(self, request, *args, **kwargs):
        '''
        Create film with given film data
        '''
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'year': request.data.get('year')
        }
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteFilmView(generics.GenericAPIView):
    '''
    API endpoints that allows users to delete films
    '''
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        moviefilm_id = kwargs.get('moviefilm_id')
        film_instance = Movie.objects.get(pk=moviefilm_id)
        if not film_instance:
            return Response(
                {"res": "Object with movie id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if film_instance:
            film_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )     
        
        