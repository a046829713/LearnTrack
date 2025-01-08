from django.db import models

# Create your models here.
from django.db import models

class MainProject(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name

class SubTask(models.Model):
    main_project = models.ForeignKey(MainProject, on_delete=models.CASCADE, related_name='sub_tasks')
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (under {self.main_project.name})"
