"""Todo app models"""
from django.shortcuts import render
from .models import Bloglinks


def get_todo_list(request):
    """ Function to render the todo list """
    items = Bloglinks.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
