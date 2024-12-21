from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('studentslist/',views.studentslist,name = 'studentslist'),
    path('student_detail/',views.student_detail,name='student_detail'),
]
