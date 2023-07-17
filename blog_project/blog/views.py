from django.shortcuts import render
# We are Using class based views
from django.views.generic import ListView
from .models import Post


# Create your views here.

# list View
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
