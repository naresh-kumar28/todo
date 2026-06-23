from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from .forms import TaskAddForm

# Create your views here.

def home(request):

    tasks = Task.objects.all().order_by('-created_at')
    completed_task = Task.objects.filter(completed=True).count()
    pending_task = Task.objects.filter(completed=False).count()

    context = {
        'tasks' : tasks,
        'completed_task' : completed_task,
        'pending_task' : pending_task,
    }
    
    return render(request, 'home.html', context)


def add_task(request):

    if request.method == 'POST':
        form = TaskAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = TaskAddForm

    context = {
        'form' : form
    }

    return render(request, 'add_task.html', context)


def edit_task(request, pk):

    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskAddForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = TaskAddForm(instance=task)

    context = {
        'form' : form
    }
    
    return render(request, 'edit_task.html', context)


def delete_task(request, pk):

    task = get_object_or_404(Task, pk=pk).delete()

    return redirect('home')


def delete_all_task(request):

    if request.method == 'POST':
        Task.objects.all().delete()

    return redirect('home')


def toggle_task(request, pk):

    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.completed = not task.completed
        task.save()

    return redirect('home')


def pending_task(request):
    tasks = Task.objects.filter(completed=False).order_by('-created_at')
    completed_task = Task.objects.filter(completed=True).count()
    pending_task = Task.objects.filter(completed=False).count()

    context = {
        'tasks' : tasks,
        'completed_task' : completed_task,
        'pending_task' : pending_task,
    }

    return render(request, 'home.html', context)



def completed_task(request):
    tasks = Task.objects.filter(completed=True).order_by('-created_at')
    completed_task = Task.objects.filter(completed=True).count()
    pending_task = Task.objects.filter(completed=False).count()

    context = {
        'tasks' : tasks,
        'completed_task' : completed_task,
        'pending_task' : pending_task,
    }

    return render(request, 'home.html', context)
