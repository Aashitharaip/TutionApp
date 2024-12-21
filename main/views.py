from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Class,Student


def index(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request,'main/index.html')


@login_required
def dashboard(request):
    class_list = Class.objects.all()
    context = {'class_list' : class_list}
    return render(request, 'main/dashboard.html',context) # nice # dont forget space # good # now urls.py

def studentslist(request):
    students_list = Student.objects.all()
    context = {'students_list' : students_list}
    return render(request,'main/studentslist.html',context)

def student_detail(request):
    students_list = Student.objects.all()
    context = {'students_list':students_list}
    return render(request,'main/student_detail.html',context)