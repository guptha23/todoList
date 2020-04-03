from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone

from . import models
# Create your views here.

def home(request):
    # return HttpResponse("<h1>Om Sai Ram</h1>")

    #Intially when page loads we grab to do items and put them on home page.

    # In order_by - actually reverses the ordering.
    all_items = models.Todo.objects.all().order_by("-cur_date")
    context = {
        "todo_items" : all_items
          }

    return render(request,"todo_list/home.html",context)

@csrf_exempt
def add_todo(request):
    print("abc")
    print(request.POST)
    cur_date = timezone.now()
    task = request.POST["task"]
    print(cur_date)
    print(task)

    created_obj = models.Todo.objects.create(cur_date=cur_date,task=task)
    print(created_obj)
    print(created_obj.id)
    length = models.Todo.objects.all().count()
    print(length)

    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    print("abc")
    print(todo_id)
    models.Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
