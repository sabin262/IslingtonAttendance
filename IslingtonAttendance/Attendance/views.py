from django.shortcuts import render
from .models import *
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
    students=Student.objects.filter(group=student_group)

    return render(request,'student_record.html',{'student':students})
