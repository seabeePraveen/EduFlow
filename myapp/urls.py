from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('parent_add',views.parent_add,name='parent_add'),
    path('teacher_add',views.teacher,name='teacher_add'),
    path('student_add',views.add_student,name='add_student'),
    path('show_student',views.show_student,name='show_student'),
    path('show_teacher',views.show_teacher,name='show_teacher'),
    path('edit_student/<str:pk>',views.edit_student,name='edit_student'),
    path('edit_teacher/<str:pk>',views.edit_teacher,name='edit_teacher'),
    path('fees',views.fees,name='fees'),
    path('fee_details/<str:pk>',views.fee_details,name='fee_details'),
    path('grades',views.show_grades,name='grades'),
    path('class_grades',views.class_grades,name='class_grades'),
    path('student_grade',views.student_grade,name='student_grade'),
    path('marks_enter/<str:sub>/<str:std>',views.marks_enter,name='marks_enter')
]