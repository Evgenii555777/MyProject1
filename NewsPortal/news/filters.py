from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter
from .models import Post


class PostFilter(FilterSet):
    added_dateCreate = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gte',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'postCategory': ['exact'],
       }





