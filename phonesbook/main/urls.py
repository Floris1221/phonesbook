from django.urls import path

from . import views


urlpatterns = [
    path('', views.person_list_view, name="list"),
    path('create/', views.create, name="create"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete_person/<int:id>", views.delete_person, name="delete_person"),
]