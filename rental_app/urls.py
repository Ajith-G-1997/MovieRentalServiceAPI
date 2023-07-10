from django.urls import path
from . views import  MovieListCreateView,MovieRetrieveUpdateDeleteView

urlpatterns = [
    path('movies',MovieListCreateView.as_view(),name="MovieListCreateView"),
    path('movies/<int:pk>/', MovieRetrieveUpdateDeleteView.as_view(), name='movie-retrieve-update-delete'),

]