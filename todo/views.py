"""Todo app models"""
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Bloglinks


class PostList(generic.ListView):
    model = Bloglinks()
    queryset = Bloglinks.objects.filter(status=1).order_by('-created_on')
    template_name = 'todo/index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug,  *args, **kwargs):
        queryset = Bloglinks.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )

def get_todo_list(request):
    """ Function to render the todo list """
    items = Bloglinks.objects.all()  # noqa
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
