from .models import Snippet,Post
from rest_framework.renderers import JSONRenderer
from .serializers import SnippetSerializer, POSTSerializer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# return Response(data)  # Renders to content type as requested by the client.
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework import status
# The @api_view decorator for working with function based views.
# The APIView class for working with class-based views.
# These wrappers provide a few bits of functionality such as making 
# sure you receive Request instances in your view, and adding context to
# Response objects so that content negotiation can be performed.




"""
Note that because we want to be able to POST to this view from clients that won't have a CSRF token we need to mark the view as csrf_exempt. This isn't something that you'd normally want to do, and REST framework views actually use more sensible behavior than this, but it'll do for our purposes right now.
"""

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()#get all snippet objects
        serializer = SnippetSerializer(snippets, many=True)#seriliser the objects many=true since multi
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



@csrf_exempt
def PostList(request):
    if request.method == 'GET':
        post = Post.objects.all()#get all snippet objects
        serializer = POSTSerializer(post, many=True)#seriliser the objects many=true since multi
        return JsonResponse(serializer.data, safe=False)#use safe when serilizing many objects

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = POSTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def PostDetails(request,pk):
    
    try:
        post=Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)
    

    if request.method == 'GET':
        serializer = POSTSerializer(post)#seriliser the objects many=true since multi
        return JsonResponse(serializer.data)#use safe when serilizing many objects

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = POSTSerializer(post,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method=='DELETE':
        post.delete()
        return HttpResponse(status=204)

#updating my post into using apiview
#using apiview enables us to use Response which determines for which content type to use
#we can format to each function which determines the format it should be diplaues eg json 
@api_view(['GET','POST'])
def secondPostList(request,format=None):
    if request.method=='GET':
        post=Post.objects.all()
        serilizer=POSTSerializer(post,many=True)
        return Response(serilizer.data)
    
    elif request.method=='POST':
        serilizer=POSTSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def secondPostListDetails(request,pk, format=None):
    try:
        post=Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method=='GET':
        serilizer=POSTSerializer(post)#not using many=True since we only have one object
        return Response(serilizer.data)
    
    elif request.method=='PUT':
        serilizer=POSTSerializer(post,data=request.data)#first arg is the  data we want to cahnge and then the chnage
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serilizer.error,status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# request.POST  # Only handles form data.  Only works for 'POST' method.
# request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.




@api_view(['GET','POST'])
def SecondSnippetList(request, format=None):
    if request.method=="GET":
        snippet=Snippet.objects.all()
        serilizer=SnippetSerializer(snippet,many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)#we dont use safe anyore bcs of response
    
    elif request.method=='POST':
        data=request.data## remplace from JSNONPaser().parse(request) since request.data offer more arbitrary data
        serlizer=SnippetSerializer(data=data)
        if serilizer.is_valid():
            serlizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.error,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def SecondSnippetDetails(request,pk, format=None):

    try:
        snippet=Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serilizer=SnippetSerializer(snippet)
        return Response(serilizer.data,status=status.HTTP_200_OK)#we dont use safe anyore bcs of response
    
    elif request.method=='PUT':
        data=request.data## remplace from JSNONPaser().parse(request) since request.data offer more arbitrary data
        serlizer=SnippetSerializer(snippet,data=data)
        if serilizer.is_valid():
            serlizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.error,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        Snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Notice that we're no longer explicitly tying our requests or responses to a given content type. request.data can handle incoming json requests, but it can also handle other formats. Similarly we're returning response objects with data, but allowing REST framework to render the response into the correct content type for us.


# format=None
# To take advantage of the fact that our responses are no longer hardwired to a single content type let's add support for format suffixes to our API endpoints. Using format suffixes gives us URLs that explicitly refer to a given format, and means our API will be able to handle URLs such as http://example.com/api/items/4.json.

#Tutorial 3: Class-based Views
#we will be using apiview

from rest_framework.views import APIView
from django.http import Http404


class snippetClassList(APIView):

    def get(self,request,format=None):
        snippet=Snippet.objects.all()
        serilizer=SnippetSerializer(snippet,many=True)
        return Response(serilizer.data)
    
    def post(self,request,format=None):
        serilizer=SnippetSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.error,status=status.HTTP_400_BAD_REQUEST)

class SnippetDetailClass(APIView):

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        serilizer=SnippetSerializer(self.get_object(pk))
        return Response(serilizer.data)
    
    def put(self,request,pk,format=None):
        serilizer=SnippetSerializer(self.get_object(pk),data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Using mixins
# One of the big wins of using class-based views is that it allows us to easily compose reusable bits of behavior.

# The create/retrieve/update/delete operations that we've been using so far are going to be pretty similar for any model-backed API views we create. Those bits of common behavior are implemented in REST framework's mixin classes.

from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# The base class provides the core functionality, and the mixin classes provide the .list() and .create() actions. We're then explicitly binding the get and post methods to the appropriate actions. Simple enough stuff so far.



#GenericAPIView is used to provide the core functionality
class snippetDetailMixins(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):

    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

# # Pretty similar. Again we're using the GenericAPIView class to provide the core functionality, and adding in mixins to provide the .retrieve(), .update() and .destroy() actions.


# Using generic class-based views
# Using the mixin classes we've rewritten the views to use slightly less code than before, but we can go one step further. REST framework provides a set of already mixed-in generic views that we can use to trim down our views.py module even more.


class SnippetgenericList(generics.ListCreateAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer

class SnippetgenericDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
