from django.shortcuts import render,redirect
#from django.http import HttpResponseRedirect
from .models import TodoListItems

def indexview(request):
   all_todo_items= TodoListItems.objects.all()

   context=  {'all_items': all_todo_items}
   return render(request, 'todo.html', context=context)

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItems(content = x)
    new_item.save()
    return redirect('indexview')

def deleteTodoView(request, i):
    y = TodoListItems.objects.get(id= i)
    y.delete()
    return redirect('indexview')