from django.http import HttpResponseRedirect
from django.urls import path, reverse_lazy

from .views import (
    PostsView, 
    PostsDetailView, 
    PostsDeleteView, 
    PostsUpdateView, 
    PostsCreateView,
)
 
app_name = "posts"

urlpatterns = [
    path('', lambda x: HttpResponseRedirect(reverse_lazy("posts:list"))), 
    path('posts/', PostsView.as_view(), name="list"),
    path('post_detail/<int:id>/', PostsDetailView.as_view(), name="detail"),
    path('post_delete/<int:id>/', PostsDeleteView.as_view(), name="delete"),
    path('post_update/<int:id>/', PostsUpdateView.as_view(), name="update"),
    path('post_create/', PostsCreateView.as_view(), name="create"), 
]


