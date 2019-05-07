from django.contrib import admin
from django.urls import path

from .views import (
    StatusAPIView,
    StatusAPIDetailView,
)

urlpatterns = [
    path('', StatusAPIView.as_view(), name='list'),
    path('<int:id>/', StatusAPIDetailView.as_view(), name='detail'),
]