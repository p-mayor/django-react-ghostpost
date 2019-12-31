from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from ghostpost_project.ghostpost_app.serializers import UserSerializer, GroupSerializer, PostSerializer

from .models import Post

from django.http import JsonResponse
from django.middleware.csrf import get_token

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})

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
    def create(self, request):
        if request.method == 'POST':
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@csrf_exempt
def like(request, post_id):
    """
    Update the likes on a post.
    """
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.likes += 1
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@csrf_exempt
def unlike(request, post_id):
    """
    Update the likes on a post.
    """
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.likes -= 1
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))