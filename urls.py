from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="todo-home"),
    path('add_todo/',views.add_todo,name="add-todo"),
    path('delete_todo/<int:todo_id>/',views.delete_todo,name="delete-todo"),
]
