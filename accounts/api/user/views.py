from django.contrib.auth import get_user_model

from rest_framework import permissions, pagination
from rest_framework.generics import RetrieveAPIView, ListAPIView

from status.api.serializers import StatusInlineUserSerializer
from accounts.api.user.serializers import UserDetailSerializer
from ..permissions import AnonPermissionOnly
from status.models import Status


User = get_user_model()


class UserDeatilAPIView(RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = "username"

    def get_serializer_context(self):
        return {'request': self.request}


class UserStatusAPIView(ListAPIView):
    serializer_class = StatusInlineUserSerializer
    # pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)
