from django.contrib import admin
from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
from .views import test_general_log
from .views import test_security_log

urlpatterns = [

    path('author_list', AuthorList.as_view()),
    path('<int:pk>', cache_page(60)(PostDetail.as_view()), name='post_detail'),
    path('news/', PostList.as_view(), name='news'),
    path('search/', PostSearch.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='create'),
    path('<int:pk>/edit/', PostCreate.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('test_error/', test_error, name='test_error'),
    path('test_general_log/', test_general_log, name='test_general_log'),
    path('test-security-log/', test_security_log, name='test_security_log'),



]