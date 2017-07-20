from django.forms import Form, ModelForm, ModelMultipleChoiceField, CharField, IntegerField, Field, DateInput
from .models import *


class DateInput(DateInput):
    input_type = 'date'


class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        exclude = ['necessary_works']
        widgets = {
            "Начало": DateInput(),
            "Окончание": DateInput()
        }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['login', 'password', 'user', 'report', 'review', 'mark']


class DiaryRecordForm(ModelForm):
    class Meta:
        model = DiaryRecord
        exclude = ['diary']
        widgets = {
            'Дата': DateInput()
        }


class IndividualTaskForm(ModelForm):
    class Meta:
        model = IndividualTask
        exclude = ['student']


class PassForm(Form):
    necessary_works = CharField(max_length=80)  # в каких видах работ нуждается
    report = TextField(max_length=1429)  # big field 1
    review = TextField(max_length=1034)  # big field 2
    mark = CharField(max_length=20)  # оценка
