from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TodoForm()
    todos = Todo.objects.all().order_by("-created_at")
    return render(request, "todos/index.html", {"todos": todos, "form": form})

def detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, "todos/detail.html", {"todo": todo})

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("index")
    return redirect("detail", pk=pk)

def toggle_completed(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.completed = not todo.completed
        todo.save()
        return redirect("detail", pk=pk)
    return redirect("detail", pk=pk)

def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("detail", pk=pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, "todos/edit.html", {"form": form, "todo": todo})