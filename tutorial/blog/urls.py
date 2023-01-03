from rest_framework.routers import DefaultRouter
from django.urls import path, include

from blog.views import AuthorViewSet, AuthorsCommentView
from blog.views import PostView
from blog.views import RecentPostView

router = DefaultRouter()

router.register("author", AuthorViewSet, basename="author")
router.register("recent/posts", RecentPostView, basename="recent-posts")
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
    path(
        'author/<int:author_pk>/comment',
        AuthorsCommentView.as_view(),
        name="author-comment"
    )
]
