from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Student
    url(r'^diary/', views.edit_diary, name='diary'),
    url(r'^diaryview/', views.diary_view, name='diaryview'),
    url(r'^reportview/', views.report_view, name='reportview'),
    url(r'^individualview1/', views.indone_view, name='individualview1'),
    url(r'^individualview2/', views.indtwo_view, name='individualview2'),
    url(r'^passview/', views.pass_view, name='passview'),
    url(r'^report/', views.edit_report, name='report'),
    url(r'^individual/', views.edit_individual, name='individual'),
    url(r'^pass/', views.edit_pass, name='pass'),
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
