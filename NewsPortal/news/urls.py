from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('author_list', AuthorList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/', PostList.as_view(), name='news'),
    path('search/', PostSearch.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='create'),
    path('<int:pk>/edit/', PostCreate.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    #path('categories/<int:pk>/subscriptions', name='subscriptions'),



]