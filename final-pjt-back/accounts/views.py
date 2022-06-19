from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def follow(request, username):
    person = get_object_or_404(User, username=username)
    if request.user.is_authenticated:
        me = request.user
        if person != me:
            if person.followers.filter(pk=me.pk).exists():
                person.followers.remove(me)
                is_follow = False
            else:
                person.followers.add(me)
                is_follow = True
            serializer = ProfileSerializer(person)
        else:
            serializer = ProfileSerializer(me)
        return Response(serializer.data)



    

