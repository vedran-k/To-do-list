from django.contrib import admin
from django.urls import path
from todoapp.views import todo_app_view, add_todo_view, delete_todo_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', todo_app_view),
    path('addTodoItem/',add_todo_view), 
    path('deleteTodoItem/<int:i>/', delete_todo_view, name = 'deletetodo'), 
]