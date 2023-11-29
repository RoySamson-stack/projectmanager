# urls.py in your project management app

from django.urls import path
from .views import project_list, project_detail

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path('projects/<int:project_id>/', project_detail, name='project_detail'),
    # Add more URLs as needed
]
