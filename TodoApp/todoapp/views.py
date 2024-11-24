from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm

def todo_list(request):
    tasks = TodoItem.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    return render(request, 'todoapp/todo_list.html', {'tasks': tasks, 'form': form})

def delete_task(request, task_id):
    task = TodoItem.objects.get(id=task_id)
    task.delete()
    return redirect('todo_list')
