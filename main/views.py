from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Class, Student, School, Fee

def index(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request,'main/index.html')


@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html', {
        "classes": Class.objects.all()
    })  


@login_required
def students(request, class_id):
    students = Student.objects.filter(class_name__id = class_id)
    _class = Class.objects.get(id = class_id)
    if request.method == "POST":
        name = request.POST.get('name')
        joining_date = request.POST.get('joining_date')
        contact_no = request.POST.get('contact_no')
        school_id = int(request.POST.get('school'))
        Student(
            name=name,
            class_name=_class,
            joining_date=joining_date,
            contact_no=contact_no,
            school=School.objects.get(id = school_id)
        ).save()
        return redirect(reverse("students", kwargs={"class_id":class_id}))

    context = {
        "students" : students, 
        "class": _class,
        "schools":School.objects.all()
    }
    return render(request,'main/students.html',context)

@login_required
def student_detail(request, id):
    student = Student.objects.get(id = id)
    if request.method == "POST":
        payment_date = request.POST.get("payment_date")
        amount = request.POST.get("amount")
        Fee(
            student = student,
            date_of_payment = payment_date,
            amount_paid = int(amount)
        ).save()
        return redirect(reverse("student_detail", kwargs={"id":id}))
    

    return render(request,'main/student_detail.html', {
        "student": student
    })

