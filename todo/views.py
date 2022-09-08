"""Todo app models"""
from django.shortcuts import render


def get_todo_list(request):
    """ Function to render the todo list """
    return render(request, 'todo/todo_list.html')
