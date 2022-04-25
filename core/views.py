from django.http import HttpResponse
from django.urls import reverse_lazy
# from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit  import CreateView, UpdateView

from .models import Like, Post 
from .forms import PostForm

# ORM-->
# Post.objects.first()
# Post.objects.last()
# post = Post.objects.get(...)
# Post.objects.all(...)
# Post.objects.filter(...)
# Post.objects.create(...)
# post.title = ...
# post.save()
# post.delete()

# def posts(requst):
#   posts = Post.objects.all() 
#   results = ", ".join([post.title for post in posts])
    # posts = "post 1: you can do it!" 
#   return HttpResponse(f'<h1>{results}</h1>')

# ------------------------------------------------------------

# class PostsView(TemplateView):
#     template_name = 'core/posts.html'
# 
#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx['posts'] = Post.objects.all()
#         return ctx 
        

class PostsView(ListView):
    template_name = 'core/posts.html'
    queryset = Post.objects.none()
    # context_object_name = 'posts' 

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.filter(user=self.request.user)
        results = [
            (
                p,
                p.like_set.filter(status=True).count(),
                p.like_set.filter(status=False).count(), 
            )
            for p in posts
        ]
        
        ctx['results'] = results

        return ctx  

class PostsDetailView(DetailView):
    queryset = Post.objects.all() 
    template_name = 'core/post_detail.html'
    pk_url_kwarg = 'id'


class PostsDeleteView(DeleteView):   
    queryset = Post.objects.all() 
    template_name = 'core/post_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("posts:list")

class PostsUpdateView(UpdateView):
    queryset = Post.objects.all() 
    template_name = 'core/post_update.html'
    pk_url_kwarg = 'id'
    fields = ['title', 'content']
    success_url = reverse_lazy("posts:list")

class PostsCreateView(CreateView):
    queryset = Post.objects.all() 
    template_name = 'core/post_create.html'
    # fields = ['title', 'content', 'user']
    success_url = reverse_lazy("posts:list")
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

 



