from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('author_list', AuthorList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/', index),

]