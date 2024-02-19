from django.urls import path
from . import views


urlpatterns = [
	path('projects/', views.projects, name='projects'),
	path('about/', views.about, name='about'),
	path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
]