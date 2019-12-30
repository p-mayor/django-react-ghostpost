from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ghostpost_project.ghostpost_app.serializers import UserSerializer, GroupSerializer, PostSerializer

from django.http import HttpResponseRedirect

from .models import Post


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def like(request, post_id):
    """
    Update the likes on a post.
    """
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.likes += 1
        post.save()
        return HttpResponseRedirect('/')
