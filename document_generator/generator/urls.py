from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^student/diary', views.edit_diary, name='diary'),
    url(r'^student/report', views.edit_report, name='report'),
    url(r'^student/individual', views.edit_individual, name='individual'),
    url(r'^student/pass', views.edit_pass, name='pass'),
    url(r'^student/', views.student_profile, name='student_profile'),
    url(r'^deanery/practices/new', views.new_practice, name='new_practice'),
    url(r'^deanery/practices/(?P<id>\d+)', views.edit_practice, name='edit_practice'),
    url(r'^deanery/practices', views.practices, name='practices'),
    url(r'^deanery/students/new', views.new_student, name='new_student'),
    url(r'^deanery/students/(?P<id>\d+)/report', views.student_report, name='student_report'),
    url(r'^deanery/students/(?P<id>\d+)/individual', views.student_individual, name='student_individual'),
    url(r'^deanery/students/(?P<id>\d+)/pass', views.student_pass, name='student_pass'),
    url(r'^deanery/students/(?P<id>\d+)', views.edit_student, name='edit_student'),
    url(r'^deanery/students', views.students, name='students'),
    url(r'^deanery', views.deanery_main, name='deanery_main'),
]

