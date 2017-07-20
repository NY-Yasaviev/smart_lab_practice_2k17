from django.forms import Form, ModelForm, ModelMultipleChoiceField, CharField, IntegerField, Field, DateInput
from .models import *


class DateInput(DateInput):
    input_type = 'date'


class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'
        widgets = {
            "Начало": DateInput(),
            "Окончание": DateInput()
        }
        labels = {
            'name': "Название практики",
            'teacher': "Руководитель практики от университета",
            'chief': "Руководитель практики от профильной организации",
            'director': "Руководитель профильной организации",
            'company': "Название организации",
            'address': "Адрес",
            'type': "Тип практики",
            'date_from': "Дата начала",
            'date_to': "Дата окончания"
        }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['login', 'password', 'user']
        labels = {
            'name': "ФИО",
            'course': "Курс",
            'group': "Группа",
            'practice': "Практика(может быть несколько)",
            'edu_profile': "Направление подготовки",
            'contract': "Наличие договора о практике",
            'status': "Квалификация"
        }

class DiaryRecordForm(ModelForm):
    class Meta:
        model = DiaryRecord
        exclude = ['diary']
        widgets = {
            'Дата': DateInput()
        }
        labels = {
            'description': "Описание выполненной работы",
            'date' : "Дата"
        }


class IndividualTaskForm(ModelForm):
    class Meta:
        model = IndividualTask
        exclude = ['student']
        labels = {
            'practice_type': "Тип практики",
            'desc': " Индивидуальное задание",
            'dateFrom': "Дата начала",
            'dateTo': "Дата окончания"
        }
