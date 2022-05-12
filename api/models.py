from django.db import models
import django_filters

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    year = models.IntegerField()
    
class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='exactname')
    
    class Meta:
        model = Movie
        fields = ['description','year']