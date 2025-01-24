from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('class/<int:class_id>/students', views.students, name = 'students'),
    path('student/<int:id>', views.student_detail, name='student_detail'),
]
