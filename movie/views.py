from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import generics
from django.db.models import Q



# class MovieListView(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

class MovieListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MovieSerializer

    def get_queryset(self):
        # breakpoint()
        queryset = Movie.objects.all()
        name = self.request.query_params.get('name', None)
        director = self.request.query_params.get('director', None)
        if name:
            # queryset = queryset.filter(name = name)
            queryset = queryset.filter(Q(name__icontains=name)).distinct()
        if director:
            queryset = queryset.filter(Q(director__icontains=director)).distinct()
        return queryset



class MovieRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

