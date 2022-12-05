from rest_framework.routers import DefaultRouter
from django.urls import path, include

from blog.views import AuthorViewSet
from blog.views import PostView

router = DefaultRouter()

router.register("author", AuthorViewSet, basename="author")
# router.register("author/<int:author_pk>/posts/", PostView, basename="post")

urlpatterns = [
    path('', include(router.urls)),
    path(
        'author/<int:author_pk>/post',
        PostView.as_view({"get": "list", "post": "create"}),
        name="post-list"
    ),
    path(
        'author/<int:author_pk>/post/<int:pk>',
        PostView.as_view({"get": "retrieve"}),
        name="post-detail"
    ),
]
