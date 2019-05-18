from django.shortcuts import render
from django.views import generic
from .models import Post

class PostIndex(generic.ListView):
	queryset = Post.objects.publié() # use "for post in object_list:" in templates to get posts
	template_name = 'blog/post.html'

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'blog/post-detail.html'
