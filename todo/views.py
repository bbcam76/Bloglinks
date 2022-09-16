"""Todo app models"""
from django.shortcuts import render
from django.views import generic
from .models import Bloglinks


def get_todo_list(request):
    """ Function to render the todo list """
    items = Bloglinks.objects.all()  # noqa
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


#class PostList(generic.ListView):
#    """ Post list views """
#    model = Bloglinks
#    queryset = Bloglinks.objects.filter(status=1).order_by('-created_on')  # noqa
#    template_name = 'index.html'
#    paginate_by = 6
