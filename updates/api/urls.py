from django.contrib import admin
from django.urls import path

from .views import (
    UpdateModelDetailAPIView,
    UpdateModelListAPIView
)

urlpatterns = [
    path('', UpdateModelListAPIView.as_view()),
    path('<int:id>/', UpdateModelDetailAPIView.as_view()),
]