from django.contrib import admin
from .models import Snippet,Note,Task,Post,Book,Author,Genre,Language
# Register your models here.

admin.site.register(Note)
admin.site.register(Task)
admin.site.register(Snippet)
admin.site.register(Post)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Language)



