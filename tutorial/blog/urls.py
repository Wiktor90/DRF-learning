from rest_framework.routers import DefaultRouter
from django.urls import path, include

from blog.views import AuthorViewSet

router = DefaultRouter()

router.register("authors", AuthorViewSet, basename="author")

urlpatterns = [path('', include(router.urls))]