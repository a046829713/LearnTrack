from django.db import models

class Node(models.Model):
    title = models.CharField(max_length=255)                 # 節點標題
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        related_name='children', 
        null=True, 
        blank=True
    )
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
