from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as rf_view

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("groups", GroupViewSet)
router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewSet,
                basename="comments")

urlpatterns = [
    path("v1/api-token-auth/", rf_view.obtain_auth_token),
    path("v1/", include(router.urls)),
]
