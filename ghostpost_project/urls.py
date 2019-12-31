from django.urls import include, path
from rest_framework import routers
from ghostpost_project.ghostpost_app import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('like/<int:post_id>', views.like, name='like'),
    path('unlike/<int:post_id>', views.unlike, name='unlike'),
    path('postlist/', views.post_list, name='postlist'),
    path('admin/', admin.site.urls),
    path('csrf/', views.csrf),
    path('ping/', views.ping),
]