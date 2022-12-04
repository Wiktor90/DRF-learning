from rest_framework.routers import DefaultRouter
from django.urls import path, include

from blog.views import AuthorViewSet
from blog.views import PostView

router = DefaultRouter()

router.register("authors", AuthorViewSet, basename="author")

urlpatterns = [
    path('', include(router.urls)),
    path('author/<int:pk>/posts', PostView.as_view(), name="post-list"),
]
