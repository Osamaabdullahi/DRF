from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('post/', views.PostList),
    path('post/<int:pk>/', views.PostDetails),
    path('secondSnippets/', views.SecondSnippetList),
    path('secondSnippets/<int:pk>/', views.SecondSnippetDetails),
    path('secondPost/', views.secondPostList),
    path('secondPost/<int:pk>/', views.secondPostListDetails),
]


urlpatterns = format_suffix_patterns(urlpatterns)
