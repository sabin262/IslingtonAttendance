from django.urls import path
from . import views


urlpatterns = [
    path('', views.faculty, name='faculty'),
    path('modules/<int:faculty>/', views.module_list,name="module_list"),
    path('group/<int:faculty_group>/', views.group_list,name="group_list"),
    path('students/<slug:student_group>/', views.student_list,name="student_list"),


]