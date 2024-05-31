from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serialized_profile = ProfileSerializer(profile, many=False)
    return Response(serialized_profile.data)

@api_view(["POST"])
@permission_classes([])
def create_user(request):
    user = User.objects.create(
        username = request.data["username"],
    )
    user.set_password(request.data["password"])
    user.save()

    profile = Profile.objects.create(
        user = user,
        first_name = request.data["first_name"],
        last_name = request.data["last_name"]
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    profile_serialized.data.token = TokenObtainPairView.as_view()
    return Response(profile_serialized.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_books(request):
    user = request.user
    books = user.book_set.all() #related name - https://docs.djangoproject.com/en/stable/topics/db/queries/#backwards-related-objects
    books_serialized = {}

    for book in books:
        book_serialized = BookSerializer(book)
        books_serialized[str(book_serialized.data["id"])] = book_serialized.data

    return Response(books_serialized)



