from rest_framework import serializers
from .models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES,Post

from  django.contrib.auth.models import User


# Because 'snippets' is a reverse relationship on the User model, it will not be included by default when using the ModelSerializer class, so we needed to add an explicit field for it.

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


#The first part of the serializer class defines the fields that get serialized/deserialized.
#The create() and update() methods define how fully fledged instances are created or modified
# when calling serializer.save()
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

# #he field flags can also control how the serializer should be displayed in certain circumstances,
# #such as when rendering to HTML. The {'base_template': 'textarea.html'} 

#     def create(self,validated_data):
#         #Create and return a new `Snippet` instance, given the validated data.
#         return Snippet.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         #Update and return an existing `Snippet` instance, given the validated data.
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
    



#It's important to remember that ModelSerializer classes don't do anything particularly magical,
# they are simply a shortcut for creating serializer classes:
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style',"owner"]

# The field we've added is the untyped ReadOnlyField class, in contrast to the other typed fields, such as CharField, BooleanField etc... The untyped ReadOnlyField is always read-only, and will be used for serialized representations, but will not be used for updating model instances when they are deserialized. We could have also used CharField(read_only=True) here.



class PostSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    content=serializers.CharField(style={"base_template":"textarea.html"})

    def create(self,validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance



class POSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']



#NOTE THERE ARE TWO WAYS OF  SERILZIG DATA 

#METHOD ONE IS USING SERILIZER CLASS
from .models import Note, Task

class NotesSerilizer(serializers.Serializer):
    title=serializers.CharField(allow_blank=True,required=True,max_length=100)
    content=serializers.CharField(style={"base_template":"textarea.html"})

    def create(self,validated_data):
        return Note.objects.create(**validated_data)
    
    def update(self,instance,validates_data):
        instance.title=validates_data.get("title".instance.title)
        instance.content=validates_data.get("content",instance.content)
        instance.save()
        return instance
    

# the second method is using the model serilizer

class TaskSerilizer(serializers.ModelSerializer):
    class Meta:
        fields=['id','title','description']
        model=Task
