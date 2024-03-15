from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('doneTask/<int:pk>/', views.doneTask, name='doneTask'),
]
