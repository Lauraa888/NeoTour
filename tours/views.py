from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Tour, Review, Application
from .serializers import (
    TourListSerializer,
    TourCreateSerializer,
    TourDetailSerializer,
    ReviewSerializer,
    ApplicationListSerializer,
    ApplicationCreateSerializer,
)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import os

# ViewSet для заявок
class ApplicationListCreateView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = TourListSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = {
        "tour__category": ["exact"],  # Фильтрация по категории тура
    }

    @swagger_auto_schema(
        operation_description="Этот эндпоинт позволяет получить "
        "список постов. Вы можете применять "
        "фильтрацию по категории, а также осуществлять "
        "поиск по заголовку и содержанию постов.",
        manual_parameters=[
            openapi.Parameter(
                "category_name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Отфильтровать посты по названию категории.",
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        print(os.getenv('CLOUD_NAME'))
        return super().get(request, *args, **kwargs)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


# Получение списка туров и создание нового тура
class TourListView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourListSerializer


class RecommendedTourView(generics.ListAPIView):
    queryset = Tour.objects.filter(recommended=True)
    serializer_class = TourListSerializer


class TourCreateView(generics.CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourCreateSerializer


# Получение детальной информации о туре
class TourDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer


# ViewSet для рецензий
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()

    serializer_class = ReviewSerializer
