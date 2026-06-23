from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('delete-all-task/', views.delete_all_task, name='delete_all_task'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('pending-task/', views.pending_task, name='pending_task'),
    path('completed-task/', views.completed_task, name='completed_task'),
]
