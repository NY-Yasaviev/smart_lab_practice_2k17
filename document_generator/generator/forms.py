from django.forms import Form, ModelForm, ModelMultipleChoiceField, CharField, IntegerField, Field
from .models import *


class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'


class DatesForm(ModelForm):
    class Meta:
        model = Dates
        exclude = ['practice']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['login', 'password', 'user']


class DiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'


class ReportForm(Form):
    company_name = CharField
    fio = CharField
    group = CharField
    teacher = CharField
    institute_practice_chief = CharField
    company_practice_chief = CharField


class PassForm(ModelForm):
    class Meta:
        model = Pass
        fields = '__all__'


class IndividualTaskForm(ModelForm):
    class Meta:
        model = IndividualTask
        fields = '__all__'


class IndividualTaskDocForm(Form):
    edu_profile = CharField
    company_name = CharField
    fio = CharField
    dateFrom = DateField
    dateTo = DateField
    institute_practice_chief = CharField
    company_practice_chief = CharField
