""" Home page views """
from django.shortcuts import render
from django.views import generic
#from .models import Post


def index(request):
    """ View to return the home/landing page """
    return render(request, 'home/index.html')


#class PostList(generic.ListView):
#    model = Post
#   queryset = Post.objects.filter(status=1).order_by("-created_on")
#    template_name = "index.html"
#   paginate_by = 6
