from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourListView, TourCreateView,TourDetailView, ReviewCreateView, ApplicationListCreateView


urlpatterns = [
    path('create/review/', ReviewCreateView.as_view()),
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('tours/', TourListView.as_view(), name='tour-list'),  # Для получения списка туров
    path('tours/create/', TourCreateView.as_view(), name='tour-create'),  # Для создания нового тура
    path('tours/<int:pk>/', TourDetailView.as_view(), name='tour-detail'),
]

