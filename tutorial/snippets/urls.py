from rest_framework.routers import DefaultRouter
from django.urls import path, include
from snippets import views

router = DefaultRouter()
router.register("users", views.UserViewSet, basename="user")
router.register("snippets", views.SnippetViewSet, basename="snippet")

urlpatterns = [path('', include(router.urls))]
