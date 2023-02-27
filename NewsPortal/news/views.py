from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import *

def index(request):
    pos = Post.objects.all()
    return render(request, 'news.html', context={'pos': pos})


class PostList(ListView):
    model = Post
    context_object_name = 'Post'
    template_name = 'news.html'


class AuthorList(ListView):
    model = Author
    context_object_name = 'Author'
    template_name = 'news/author_list.html'

class PostDetail(DetailView):
    model = Post
    context_object_name = 'Post'
    template_name = 'post_detail.html'

class CategoryList(ListView):
    model = Category
    context_object_name = 'Category'

class PostCategory(DetailView):
    model = PostCategory
    context_object_name = 'PostCategory'

class CommentDetail(DetailView):
    model = Comment
    context_object_name = 'Comment'
