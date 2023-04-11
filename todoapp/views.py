from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoListItem

def todo_app_view(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})

def add_todo_view(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def delete_todo_view(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 
