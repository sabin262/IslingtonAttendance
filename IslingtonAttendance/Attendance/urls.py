from django.urls import path
from . import views


urlpatterns = [
    path('', views.faculty, name='faculty'),
    path('modules/<int:faculty>/', views.module_list,name="module_list"),
    path('<int:faculty_group>/', views.group_list,name="group_list"),


]