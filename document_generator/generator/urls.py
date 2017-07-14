from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^diary/', views.edit_diary, name='diary'),
    url(r'^report/', views.edit_report, name='report'),
    url(r'^individual/', views.edit_individual, name='individual'),
    url(r'^pass/', views.edit_pass, name='pass'),
    url(r'^practices/new/', views.new_practice, name='new_practice'),
    url(r'^practices/(?P<id>\d+)/', views.edit_practice, name='edit_practice'),
    url(r'^practices/', views.practices, name='practices'),
    url(r'^students/new/', views.new_student, name='new_student'),
    url(r'^students/(?P<id>\d+)/report/', views.student_report, name='student_report'),
    url(r'^students/(?P<id>\d+)/individual/', views.student_individual, name='student_individual'),
    url(r'^students/(?P<id>\d+)/pass/', views.student_pass, name='student_pass'),
    url(r'^students/(?P<id>\d+)/', views.edit_student, name='edit_student'),
    url(r'^students/', views.students, name='students'),
]

