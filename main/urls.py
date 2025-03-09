from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("projects/with-tag/<str:tag>/", views.projects, name="projects-withtag"),
]