from django.conf.urls import url
from . import views

urlpatterns = [
    # Student
    url(r'^practice_(?P<id>\d+)/diary_view/', views.diary_view, name='diary_view'),
    url(r'^practice_(?P<id>\d+)/diary/new/', views.new_diary_record, name='new_diary_record'),
    url(r'^practice_(?P<id>\d+)/diary/record_(?P<record_id>\d+)/', views.edit_record, name='edit_record'),
    url(r'^practice_(?P<id>\d+)/diary/d/', views.diary_download, name='diary_download'),
    url(r'^practice_(?P<id>\d+)/diary/', views.diary, name='diary'),
    url(r'^practice_(?P<id>\d+)/report_view/', views.report_view, name='report_view'),
    url(r'^practice_(?P<id>\d+)/report/d/', views.report_download, name='report_download'),
    url(r'^practice_(?P<id>\d+)/individual_view/', views.individual_view, name='individual_view'),
    url(r'^practice_(?P<id>\d+)/individual/d/', views.individual_download, name='individual_download'),
    url(r'^practice_(?P<id>\d+)/individual/', views.edit_individual, name='individual'),
    url(r'^practice_(?P<id>\d+)/pass_view/', views.pass_view, name='pass_view'),
    url(r'^practice_(?P<id>\d+)/pass/d/', views.pass_download, name='pass_download'),
    url(r'^practice_(?P<id>\d+)/pass/', views.edit_pass, name='pass'),
    url(r'^practice_(?P<id>\d+)/', views.practice_docs, name='practice_docs'),
    url(r'^profile/', views.profile, name='profile'),
    # Deanery
    url(r'^ind_tasks/(?P<id>\d+)/', views.ind_edit, name='new_ind'),
    url(r'^ind_tasks/add/(?P<type>\w+)/', views.new_ind, name='new_ind'),
    url(r'^ind_tasks/', views.ind_list, name='ind_list'),
    url(r'^practices/new/', views.new_practice, name='new_practice'),
    url(r'^practices/(?P<id>\d+)/', views.edit_practice, name='edit_practice'),
    url(r'^practices/', views.practices, name='practices'),
    url(r'^students/new/', views.new_student, name='new_student'),
    url(r'^students/(?P<id>\d+)/', views.edit_student, name='edit_student'),
    url(r'^students/', views.students, name='students'),
]
