from django.urls import path
from . import views



urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('modules/<int:faculty>/', views.module_list,name="module_list"),
    path('group/<slug:faculty_group>/', views.group_list,name="group_list"),
    path('students/<slug:student_group>/', views.student_list,name="student_list"),
    path('authenticate', views.authenticateUser, name='authenticate_user')



]