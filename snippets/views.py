from .models import Snippet,Post
from django.contrib.auth.models import User
from .serializers import SnippetSerializer,UserSerializer,PostSerilizer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action




@api_view(['GET'])
def api_root(request):
    return Response({
        'users': reverse('user-list', request=request),
        'snippets': reverse('snippet-list', request=request)
    })


# class UserList(generics.ListAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class UserDetails(generics.RetrieveAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class SnippetList(generics.ListCreateAPIView):
#     queryset=Snippet.objects.all()
#     serializer_class=SnippetSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class SnipetsDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Snippet.objects.all()
#     serializer_class=SnippetSerializer

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)


class UserViewset(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class SnippetViewset(viewsets.ModelViewSet):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


    

class PostViewset(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerilizer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

