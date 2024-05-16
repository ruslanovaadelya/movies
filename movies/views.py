from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Movie
from .serializers import MovieSerializer


class MovieList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
