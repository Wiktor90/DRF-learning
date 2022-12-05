from rest_framework.routers import DefaultRouter
from django.urls import path, include

from blog.views import AuthorViewSet
from blog.views import PostView

router = DefaultRouter()

router.register("authors", AuthorViewSet, basename="author")
# router.register("author/<int:author_pk>/posts", PostView, basename="post")

urlpatterns = [
    path('', include(router.urls)),
    path('author/<int:author_pk>/posts', PostView.as_view({"get":"list"}), name="post-list"),
    path(
        'author/<int:author_pk>/posts/<int:pk>',
        PostView.as_view({"get":"retrieve"}),
        name="post-detail"
    ),
]
