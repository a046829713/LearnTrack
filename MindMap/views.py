from django.shortcuts import render
from django.views import View
from .models import Node

class Index(View):
    def get(self, request):
        return render(request, 'mindmap/index.html', {})


class AddMindMap(View):
    def get(self, request):
        # 取得所有節點
        nodes = Node.objects.all()
        # 回傳給前端模板

        print(nodes)
        return render(request, 'mindmap/addMindMap.html', {
            'nodes': nodes
        })