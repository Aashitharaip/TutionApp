from django.contrib import admin
from main.models import Class, Student, School, Fee

admin.site.site_title = 'Tution Tracker'
admin.site.index_title = 'Tution Tracker'
admin.site.site_header = 'Tution Tracker Administration'

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "_class", "joining_date", "contact_no")
    list_filter = ('_class',)


@admin.register(Fee)
class FeesAdmin(admin.ModelAdmin):
    list_display = ("student", "amount_paid", "date_of_payment")


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass



