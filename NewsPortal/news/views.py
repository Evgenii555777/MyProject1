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
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.models import Exists, OuterRef
import logging
from django.utils.translation import gettext as _

logger = logging.getLogger('django')

logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message', exc_info=True)
logger.critical('Critical message', exc_info=True)

#from .task import add

#def new_add(request):




def index(request):
    pos = Post.objects.all()
    return render(request, 'news.html', context={'pos': pos})


class PostList(ListView):
    model = Post
    context_object_name = 'pos'
    template_name = 'news.html'
    paginate_by = 10


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

@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )


class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.postCategory = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory=self.postCategory).order_by('-dateCreation')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.postCategory.subscribers.all()
        context['category'] = self.postCategory
        return context


@login_required
def subsribe(request, pk):
    user = request.user
    categoru = Category.objects.get(id=pk)
    categoru.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'news/subscribe.html', {'category': categoru, 'message': massage})

def test_error(request):
    try:
        x = 1 / 0  # Это вызовет ошибку ZeroDivisionError
    except ZeroDivisionError as e:
        logger = logging.getLogger('django.request')  # Получить логгер 'django.request'
        logger.error('Ошибка деления на ноль', exc_info=True)  # Запись ошибки в лог
        return HttpResponse('Ошибка деления на ноль')  # Отправить сообщение об ошибке пользователю

def test_general_log(request):
    logger = logging.getLogger('django')  # Получить логгер 'django'
    logger.info('Тестовая запись в general.log')  # Записать тестовое сообщение
    return HttpResponse('Тестовая запись выполнена')

def test_security_log(request):
    logger = logging.getLogger('django.security')
    logger.debug('Тестовая запись в security.log')
    return HttpResponse('Тестовая запись в security.log создана')

class Index(View):
    def get(self, request):
        # . Translators: This message appears on the home page only
        models = MyModel.objects.all()

        context = {
            'models': models,
        }

        return HttpResponse(render(request, 'index2.html', context))


