from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.db import  transaction
from .forms import * 
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login_page(request):
	return render(request,'Attendance/login_page.html')

def faculty(request):
    faculties=Faculty.objects.all()
    return render(request, 'Attendance/faculty.html', {'faculties': faculties})

def module_list(request,faculty):
    modules = Faculty_Module_Group.objects.prefetch_related('module').filter(faculty_id=faculty)
    return render(request,'Attendance/modules.html', {'modules':modules})


def group_list(request,faculty_group):
    facult=Faculty_Module_Group.objects.get(module=faculty_group)
    print("Faculty: ",facult.faculty)
    group=Group.objects.filter(faculty_id=facult.faculty)

    return render(request, 'Attendance/group.html', {'groups':group})

def student_list(request,student_group):
    students=Student_group.objects.prefetch_related('student').filter(group=student_group)

    return render(request,'Attendance/student_record.html',{'student':students})



def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def authenticateUser(request):
    
    username = request.POST['username']
    password = request.POST['pass']
    print("Credentials: ",username,"  ",password)

    user = authenticate(request, username=username, password=password)
    if user is not None:
       # modules = Teacher_Module.objects.prefetch_related('module').filter(faculty_id=faculty)
        userId=User.objects.get(username=username)
        print(userId.id)
        teacher_id=Teacher.objects.get(username_id=userId.id)
        print(teacher_id.teacher_id)
        modules = Teacher_Module.objects.prefetch_related('module').filter(teacher_id=teacher_id.teacher_id)
        return render(request, 'modules.html', {'modules': modules})
        
    else:
        # Return an 'invalid login' error message.
        return login_page(request)
