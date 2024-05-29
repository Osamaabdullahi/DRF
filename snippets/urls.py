from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # path('post/', views.PostList),
    # path('post/<int:pk>/', views.PostDetails),
    # path('secondSnippets/', views.SecondSnippetList),
    # path('secondSnippets/<int:pk>/', views.SecondSnippetDetails),
    # path('secondPost/', views.secondPostList),
    # path('secondPost/<int:pk>/', views.secondPostListDetails),
    # path('snippetClass/', views.snippetClassList.as_view()),
    # path('snippetClass/<int:pk>/', views.SnippetDetailClass.as_view()),
    # path('SnippetgenericList/', views.SnippetgenericList.as_view()),
    # path('SnippetgenericList/<int:pk>/', views.SnippetgenericDetails.as_view()),
    # path("notes/",views.NotesList),
    # path("notes/<int:pk>/",views.NoteDetails),
    # path("task/",views.TaskList),
    # path("task/<int:pk>/",views.TaskDetails),
 
    # path("NotesClassList/",views.NotesClassList.as_view()),
    # path("NotesClassList/<int:pk>/",views.NotesDeailClass.as_view()),
    # path("TaskListClass/",views.TaskListClass.as_view()),
    # path("TaskListClass/<int:pk>/",views.TaskDetailsClass.as_view()),

    # path("FinalNotes/",views.FinalNotes.as_view()),
    # path("FinalNotes/<int:pk>/",views.FinalNotesDetails.as_view()),

    # path("FinalTask/",views.FinalTask.as_view()),
    # path("FinalTask/<int:pk>/",views.FinalTaskDetail.as_view())
    
]

    
 


urlpatterns = format_suffix_patterns(urlpatterns)
