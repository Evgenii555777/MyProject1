from .models import *
from modeltranslation.translator import register, TranslationOptions

@register(MyModel)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text',)