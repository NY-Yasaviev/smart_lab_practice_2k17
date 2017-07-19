from django.forms import Form, ModelForm, ModelMultipleChoiceField, CharField, IntegerField, Field, DateInput
from .models import *


class DateInput(DateInput):
    input_type = 'date'


class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'
        widgets = {
            "start": DateInput(),
            "end": DateInput()
        }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['login', 'password', 'user']


class DiaryRecordForm(ModelForm):
    class Meta:
        model = DiaryRecord
        fields = '__all__'
        widgets = {
            "record": DateInput()
        }


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
        exclude = ['task_number', 'doc', 'type']


class IndividualTaskDocForm(Form):
    class Meta:
        model = IndividualTaskDoc
        fields = []


class ReportDocForm(ModelForm):
    class Meta:
        model = Report
        fields = []
