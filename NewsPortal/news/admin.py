from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

class CategoryAdmin(TranslationAdmin):
    model = Category

class PostAdmin(TranslationAdmin):
    model = Post

class CommentAdmin(TranslationAdmin):
    model = Comment

class MyModelAdmin(TranslationAdmin):
    model = MyModel



admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Subscriber)
admin.site.register(MyModel, MyModelAdmin)





