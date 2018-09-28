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

def faculty(request):
    faculties=Faculty.objects.all()
    return render(request, 'faculty.html', {'faculties': faculties})

def module_list(request,faculty):
    modules = Faculty_Module_Group.objects.prefetch_related('module').filter(faculty_id=faculty)
    # mods = modules[0].faculty_id
    # mods = Faculty_Module_Group.objects.prefetch_related('module_id').prefetch_related('student_id').filter

    return render(request,'modules.html', {'modules':modules})


def group_list(request,faculty_group):
    group=Group.objects.filter(faculty_id=faculty_group)

    return render(request, 'group.html', {'groups':group})

def student_list(request,student_group):
    students=Student_group.objects.prefetch_related('student').filter(group=student_group)

    return render(request,'student_record.html',{'student':students})
