from django.forms import ModelForm
from .models import *


class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'


class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['login', 'password', 'user']


class DiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'


class PassForm(ModelForm):
    class Meta:
        model = Pass
        fields = '__all__'


class DatesForm(ModelForm):
    class Meta:
        model = Dates
        fields = '__all__'


class IndividualTaskForm(ModelForm):
    class Meta:
        model = IndividualTask
        fields = '__all__'



