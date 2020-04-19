from django.urls import path
from . import views

app_name = 'planner'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>', views.detail, name='detail'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('create', views.create, name='create'),
    path('checkbox/<int:task_id>', views.checkbox, name='checkbox'),
    path('delete/<int:task_id>', views.delete, name='delete')
]
