from django.shortcuts import render
from django.views import View
from .models import Node
from django.http import JsonResponse
import json
from .models import MindMap
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
    

def save_mindmap(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            
            mindmap_id = data.get("id")
            if mindmap_id is None:

            mindmap = MindMap.objects.create()
            # 0) 找到對應的 mindmap
            mindmap = MindMap.objects.get(pk=mindmap_id)

            # 1) 清除舊的資料 (若是"更新"模式)
            #    或者你要做差異更新也可以，依需求而定
            mindmap.nodes.all().delete()
            mindmap.links.all().delete()

            # 2) 先寫入 Node
            front_id_to_db_id = {}
            new_nodes = []
            for n in data['nodes']:
                node_obj = Node(
                    mindmap=mindmap,
                    title=n.get('title', ''),
                    content=n.get('content', ''),
                    x=n.get('x'),
                    y=n.get('y'),
                    vx=n.get('vx'),
                    vy=n.get('vy'),
                    index=n.get('index')
                )
                new_nodes.append(node_obj)
            Node.objects.bulk_create(new_nodes)

            # bulk_create 不會自動給你回填 pk，所以要再查一次
            # 這裡假設 node 數量不大，否則可以自行維護
            saved_nodes = Node.objects.filter(mindmap=mindmap)
            # 依照 title 或其他欄位與前端 id 對應
            for node_obj in saved_nodes:
                # 這裡假設我們用 (title) 或 (index) 來對應前端的 node
                # 如果你 front_id 就是 "nodeX" 也可存 Node 時順便一起存到某欄位
                # 這段對照碼要依你實際需求來寫
                matched = next((n for n in data['nodes'] if n['title'] == node_obj.title), None)
                if matched:
                    front_id_to_db_id[matched['id']] = node_obj.id

            # 3) 再寫入 Link
            new_links = []
            for l in data['links']:
                # 先透過 front_id_to_db_id 找到 source / target Node 的 pk
                source_id = front_id_to_db_id.get(l['source']['id'])
                target_id = front_id_to_db_id.get(l['target']['id'])
                if source_id and target_id:
                    link_obj = Link(
                        mindmap=mindmap,
                        source_id=source_id,
                        target_id=target_id
                    )
                    new_links.append(link_obj)
            Link.objects.bulk_create(new_links)

            return JsonResponse({"status": "ok", "message": "MindMap saved"}, status=200)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=405)