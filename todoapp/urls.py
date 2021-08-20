from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexview, name= "indexview"),
    path('addTodoItem/', views.addTodoView, name='addTodoView'),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView, name= 'deleteTodoView'),
]