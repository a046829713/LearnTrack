from django.db import models

class MindMap(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Node(models.Model):
    mindmap = models.ForeignKey(
        MindMap,
        on_delete=models.CASCADE,
        related_name='nodes'
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    vx = models.FloatField(null=True, blank=True)
    vy = models.FloatField(null=True, blank=True)
    index = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Link(models.Model):
    mindmap = models.ForeignKey(
        MindMap,
        on_delete=models.CASCADE,
        related_name='links'
    )
    source = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        related_name='links_from'
    )
    target = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        related_name='links_to'
    )

    def __str__(self):
        return f"{self.source.title} -> {self.target.title}"
