from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'
router = DefaultRouter()
router.register(r'posts', PostViewSet) # GET, POST
router.register(r'groups', GroupViewSet) # GET
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)  # GET, POST

for url in router.urls:
    print(url)
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token)
]