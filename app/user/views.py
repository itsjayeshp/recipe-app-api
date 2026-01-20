"""
Views for the user API.
"""

# reminder all model , admin and migration will be handle in core app

from rest_framework import generics

from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """ Create a new user in the system """
    serializer_class = UserSerializer










