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



def student_list(request):
	students = Student.objects.all()
	groups = Group.objects.all()
	return render(request, 'Attendance/student_list.html',{'students' : students, 'groups' : groups})

def module_list(request):
	modules = Module.objects.all()
	return render(request, 'Attendance/module_list.html',{'modules' : modules})

def login_page(request):

    return render(request,'Attendance/login_page.html')



def faculty(request):
    faculties=Faculty.objects.all()
    return render(request, 'faculty.html', {'faculties': faculties})

def module_list(request,faculty):
    modules = Faculty_Module_Group.objects.prefetch_related('module').filter(faculty_id=faculty)
    return render(request,'modules.html', {'modules':modules})


def group_list(request,faculty_group):
    group=Group.objects.filter(faculty_id=faculty_group)

    return render(request, 'group.html', {'groups':group})

def student_list(request,student_group):
    students=Student_group.objects.prefetch_related('student').filter(group=student_group)

    return render(request,'student_record.html',{'student':students})



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

    user = authenticate(request, username=username, password=password)
    if user is not None:
        return render(request, 'modules.html')
        
    else:
        # Return an 'invalid login' error message.
        return login_page(request)