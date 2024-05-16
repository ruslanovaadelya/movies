from django.urls import path
from .views import MovieList, MovieDetail

urlpatterns = [
    path('<int:pk>/', MovieDetail.as_view()),
    path('', MovieList.as_view()),

]
