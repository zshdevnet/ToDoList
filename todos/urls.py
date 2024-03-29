from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('doneTask/<int:pk>/', views.doneTask, name='doneTask'),
    path('undoneTask/<int:pk>/', views.undoneTask, name='undoneTask'),
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
    path('delTask/<int:pk>/', views.delTask, name='delTask')
]
