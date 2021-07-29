from django.shortcuts import render
from rest_framework import status, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters

from business_api import permissions, serializers, models


class LoginApiView(APIView):
    serializer_class = serializers.RegisterSerializer
    queryset = models.Business.objects.all()

    def post(self, request):
        """create a new user"""
        serializer = self.serializer_class(data=request.data)


class RegisterViewSet(viewsets.ModelViewSet):
    """handle creating and updating a business user"""
    serializer_class = serializers.RegisterSerializer
    queryset = models.Business.objects.all()

    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.AccessOwnProfile,)

    http_method_names = ['post']

    """
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )
    """

    """
    def retrieve(self, request, pk=None):
        return Response(None)
    """


class LoginApiView(ObtainAuthToken):
    """handling creating business authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


"""
class BusinessFeedViewSet(viewsets.ModelViewSet):
#   Handles creating, reading and updating profile feed items
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.BusinessFeedItemSerializer
    queryset = models.BusinessFeedItem.objects.all()

    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('status_text', 'created_on')

    def perform_create(self, serializer):
#       Sets the user profile to the logged in user
        serializer.save(business=self.request.user)

"""


class FormViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating form"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.FormSerializer
    queryset = models.Form.objects.all()

    permission_classes = (
        permissions.AccessOwnProfile,
        IsAuthenticated
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(business=self.request.user)


class PartViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating part"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.PartSerializer
    queryset = models.Part.objects.all()

    permission_classes = (
        permissions.AccessOwnFormPart,
        IsAuthenticatedOrReadOnly
    )

    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(business=self.request.user)


