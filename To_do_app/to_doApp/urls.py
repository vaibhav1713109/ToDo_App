from django.urls import path
from . import views


urlpatterns = [
    path('', views.HelloWorld, name='list'),
    path('update_task/<str:pk>/',views.UpdateTask, name='update_task'),
    path('delete_task/<str:pk>/',views.DeleteItem, name='delete_item')
]