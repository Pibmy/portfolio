from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('skills/', views.all_skills),
    path('skills/<int:id>/', views.skill),
    path('projects/', views.all_projects),
    path('projects/<int:id>/', views.project),
]
