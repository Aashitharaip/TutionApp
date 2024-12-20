from django.db import models

class Class(models.Model):
    """
    Class Table consists of list of class names of students 
    It is constant table and can only be edited or added using
    Admin panel.

    Eg.: Nursery - 10th standard
    """
    name = models.CharField("Student Class", max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Classes'
        


class School(models.Model):
    """
    Table consisting of School Names
    """
    name = models.CharField("School Name", max_length=40)

    def __str__(self):
        return self.name
    
    
class Student(models.Model):
    """
    Student Table consists of details such as Student name,Date
    of joining and Parent's contact number of the respective
    students.
    """
    name = models.CharField("Student's Name", max_length=255)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    joining_date  = models.DateField("Date of Joining")
    contact_no = models.CharField("Parent's Contact No",max_length=10)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    


class Fee(models.Model):
    """
    This table is used to enter the fees given by the student
    """
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date_of_payment = models.DateField("Date of Payment")
    amount_paid = models.IntegerField("Amount Paid")
    
    def __str__(self):
        return f"{self.student.name} - {self.amount_paid}"    

