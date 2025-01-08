from django.shortcuts import render, redirect
from django.views import View
# from .models import Task  # 假設您有一個名為 Task 的模型
# from .forms import TaskForm  # 假設您有一個 TaskForm 表單

class TaskAdd(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_add.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # 假設有一個 task_list 的 URL 名稱
        return render(request, 'task_add.html', {'form': form})


class Index(View):
    def get(self, request):
        return render(request, 'StudyTrack/index.html', {})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # 假設有一個 task_list 的 URL 名稱
        return render(request, 'task_add.html', {'form': form})