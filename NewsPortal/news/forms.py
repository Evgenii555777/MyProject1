from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['postCategory', 'author', 'title','text', ]


       def clean(self):


           cleaned_data = super().clean()
           title = cleaned_data.get("title")
           text = cleaned_data.data.get("text")

           if title == text:

               raise ValidationError(
                "Описание не должно быть идентично названию."
            )


           return cleaned_data




