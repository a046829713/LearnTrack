from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('TaskAdd/', views),
    path('index/', views.Index.as_view(),name='index'),
    path('addMindMap/', views.AddMindMap.as_view(),name='addMindMap'),
]