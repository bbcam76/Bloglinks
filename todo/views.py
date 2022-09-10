"""Todo app models"""
from django.shortcuts import render
from .models import Item


def get_todo_list(request):
    """ Function to render the todo list """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
