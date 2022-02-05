from app1 import views
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('firstindex/', views.firstindex, name='firstindex'),
    # path('secondindex/', views.secondindex, name='secondindex'),

    path("", views.ListTodoAPIView.as_view(), name="todo_list"),
    path("create/", views.CreateTodoAPIView.as_view(), name="todo_create"),
    path("update/<int:pk>/", views.UpdateTodoAPIView.as_view(), name="update_todo"),
    path("delete/<int:pk>/", views.DeleteTodoAPIView.as_view(), name="delete_todo")
]
