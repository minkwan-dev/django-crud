from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/delete/", views.delete_todo, name="delete"),
    path("<int:pk>/toggle/", views.toggle_completed, name="toggle"),
    path("<int:pk>/edit/", views.edit_todo, name="edit"),
    path("<int:pk>/", views.detail, name="detail"),
    path("", views.index, name="index"),
]
