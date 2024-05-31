from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewset, basename='snippet')
router.register(r'users', views.UserViewset, basename='user')
router.register(r'post', views.PostViewset, basename='post')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]