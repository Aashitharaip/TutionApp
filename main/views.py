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
    context = {'students' : students}
    return render(request,'main/students.html',context)

@login_required
def student_detail(request, id):
    return render(request,'main/student_detail.html', {
        "student": Student.objects.get(id = id)
    })

@login_required
def add_fees(request, student_id):
    if request.method == "POST":
        payment_date = request.POST.get("payment_date")
        amount = request.POST.get("amount")
        Fee(
            student = Student.objects.get(id = student_id),
            date_of_payment = payment_date,
            amount_paid = int(amount)
        ).save()
        return redirect(reverse("student_detail", kwargs={"id":student_id}))
    return render(request, 'main/add_fees.html')

@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        class_name_id = request.POST.get('class_name')
        joining_date = request.POST.get('joining_date')
        contact_no = request.POST.get('contact_no')
        school_id = request.POST.get('school')

        class_name = Class.objects.filter(id=class_name_id).first()
        if not class_name:
            return render(request, 'main/add_student.html', {'error': 'The class you selected does not exist.'})
        school = School.objects.filter(id=school_id).first()
        if not school:
            return render(request, 'main/add_student.html', {'error': 'The school you selected does not exist.'})
        new_student = Student(
            name=name,
            class_name=class_name,
            joining_date=joining_date,
            contact_no=contact_no,
            school=school
        )
        new_student.save()
        students = Student.objects.filter(class_name=class_name)
        return render(request, 'main/studentslist.html', {'students': students, 'class_name': class_name})
    else:
        classes = Class.objects.all()
        schools = School.objects.all()
        return render(request, 'main/add_student.html', {'classes': classes, 'schools': schools})
