from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Student
    url(r'^practice_(?P<id>\d+)/diary_view/', views.diary_view, name='diary_view'),
    url(r'^practice_(?P<id>\d+)/diary/', views.edit_diary, name='diary'),
    url(r'^practice_(?P<id>\d+)/report_view/', views.report_view, name='report_view'),
    url(r'^practice_(?P<id>\d+)/report/', views.edit_report, name='report'),
    url(r'^practice_(?P<id>\d+)/individual_view/', views.individual_view, name='individual_view'),
    url(r'^practice_(?P<id>\d+)/individual/', views.edit_individual, name='individual'),
    url(r'^practice_(?P<id>\d+)/pass_view/', views.pass_view, name='pass_view'),
    url(r'^practice_(?P<id>\d+)/pass/', views.edit_pass, name='pass'),
    url(r'^practice_(?P<id>\d+)/', views.practice_docs, name='practice_docs'),
    # Deanery
    url(r'^ind_tasks/(?P<id>\d+)/', views.ind_edit, name='new_ind'),
    url(r'^ind_tasks/add/(?P<type>\w+)/', views.new_ind, name='new_ind'),
    url(r'^ind_tasks/', views.ind_list, name='ind_list'),
    url(r'^practices/new/', views.new_practice, name='new_practice'),
    url(r'^practices/(?P<id>\d+)/', views.edit_practice, name='edit_practice'),
    url(r'^practices/', views.practices, name='practices'),
    url(r'^students/new/', views.new_student, name='new_student'),
    url(r'^students/(?P<id>\d+)/report/(?P<rep_id>\d+)/', views.student_report, name='student_report'),
    url(r'^students/(?P<id>\d+)/report/', views.reports, name='reports'),
    url(r'^students/(?P<id>\d+)/individual/(?P<ind_id>\d+)/', views.student_individual, name='student_individual'),
    url(r'^students/(?P<id>\d+)/individual/', views.inds, name='inds'),
    url(r'^students/(?P<id>\d+)/pass/(?P<pass_id>\d+)/', views.student_pass, name='student_pass'),
    url(r'^students/(?P<id>\d+)/pass/', views.passes, name='passes'),
    url(r'^students/(?P<id>\d+)/', views.edit_student, name='edit_student'),
    url(r'^students/', views.students, name='students'),
]
