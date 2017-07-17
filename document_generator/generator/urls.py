from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Student
    url(r'^diary/(?P<id>\d+)/', views.edit_diary, name='diary'),
    url(r'^diary/', views.diaries, name='diaries'),
    url(r'^report/(?P<id>\d+)/', views.edit_report, name='report'),
    url(r'^report/', views.reports, name='reports'),
    url(r'^individual/(?P<id>\d+)/', views.edit_individual, name='individual'),
    url(r'^individual/', views.inds, name='individuals'),
    url(r'^pass/(?P<id>\d+)/', views.edit_pass, name='pass'),
    url(r'^pass/', views.passes, name='passes'),
    # Deanery
    url(r'^practices/new/', views.new_practice, name='new_practice'),
    url(r'^practices/(?P<id>\d+)/', views.edit_practice, name='edit_practice'),
    url(r'^practices/', views.practices, name='practices'),
    url(r'^students/new/', views.new_student, name='new_student'),
    url(r'^students/(?P<id>\d+)/report/(?P<rep_id>)/', views.student_report, name='student_report'),
    url(r'^students/(?P<id>\d+)/report/', views.reports, name='reports'),
    url(r'^students/(?P<id>\d+)/individual/(?P<ind_id>)/', views.student_individual, name='student_individual'),
    url(r'^students/(?P<id>\d+)/individual/', views.inds, name='inds'),
    url(r'^students/(?P<id>\d+)/pass/(?P<pass_id>)/', views.student_pass, name='student_pass'),
    url(r'^students/(?P<id>\d+)/pass/', views.passes, name='passes'),
    url(r'^students/(?P<id>\d+)/', views.edit_student, name='edit_student'),
    url(r'^students/', views.students, name='students'),
]
