from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import *
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin



def index(request):
    pos = Post.objects.all()
    return render(request, 'news.html', context={'pos': pos})


class PostList(ListView):
    model = Post
    context_object_name = 'pos'
    template_name = 'news.html'
    paginate_by = 10

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('news')

class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'create.html'

class PostSearch(ListView):
    model = Post
    ordering = ['title']
    template_name = 'search.html'
    context_object_name = 'post'

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = PostFilter(self.request.GET, queryset)
       return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context



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

class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'create.html'


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'create.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_post',)
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('news/news')






