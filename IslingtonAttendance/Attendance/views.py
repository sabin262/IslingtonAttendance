from django.shortcuts import render
from .models import *


def student_list(request):
	students = Student.objects.all()
	groups = Group.objects.all()
	return render(request, 'Attendance/student_list.html',{'students' : students, 'groups' : groups})

def module_list(request):
	modules = Module.objects.all()
	return render(request, 'Attendance/module_list.html',{'modules' : modules})

def login_page(request):
	return(request,'Attenadnce/login_page.html')
# Create your views here.
