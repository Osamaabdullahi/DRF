from rest_framework import serializers
from .models import Snippet,Post
from django.contrib.auth.models import User




class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(view_name='snippet-detail', many=True,read_only=True)
    post=serializers.HyperlinkedIdentityField(view_name="post-detail",many=True,read_only=True)
    class Meta:
        fields=['id','username','email','snippets','post']
        model=User

class PostSerilizer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source="owner.username")
    class Meta:
        fields="__all__"
        model=Post
 