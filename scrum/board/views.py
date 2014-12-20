from rest_framework import viewsets, authentication, permissions
from django.contrib.auth import get_user_model

from .models import Sprint, Task
from .serializers import SprintSerializer, TaskSerializer, UserSerializer


User = get_user_model()


class DefaultsMixin(object):
    """ Default settings for view authentication, permissions,
    filtering and pagination. """

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate = 100



class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint forl listing and creating task. """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing user. """

    lookup_field =  User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer


class SprintViewSet(viewsets.ModelViewSet):
    """ Api end pint for creating and listing sprint. """

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer