from django.urls import path
from . import views

urlpatterns = [
	path('', views.student_list, name='student_list'),
	path('modules',views.module_list, name='module_list'),
]