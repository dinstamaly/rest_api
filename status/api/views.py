import json

from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView
)

from status.models import Status
from accounts.api.permissions import IsOwnerOrReadOnly
from .serializers import StatusSerializer


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class StatusAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, RetrieveAPIView):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset                 = Status.objects.all()
    serializer_class         = StatusSerializer
    lookup_field             = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusAPIView(mixins.CreateModelMixin, ListAPIView):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class        = StatusSerializer
    search_fields           = ('user__username', 'content')
    ordering_fields         = ('user__username', 'timestamp')
    queryset                = Status.objects.all()

    # def get_queryset(self):
    #     request = self.request
    #     print(request.user)
    #     qs = Status.objects.all()
    #     query = request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(
    #             Q(user__username__icontains=query) |
    #             Q(content__icontains=query)
    #         )
    #     return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

