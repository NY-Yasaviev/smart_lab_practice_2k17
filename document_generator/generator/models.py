from django.db.models import Model, DateField, CharField, IntegerField, ForeignKey, ManyToManyField, OneToOneField, \
    CASCADE, TextField, BooleanField
from django.contrib.auth.models import User, Group



class Type(Model):
    name = CharField(max_length=20, null=True)
    company = CharField(max_length=60, null=True)
    address = CharField(max_length=60, null=True)


class Practice(Model):
    name = CharField(max_length=60, null=True)
    teacher = CharField(max_length=60, null=True)
    director = CharField(max_length=60, null=True)
    type = OneToOneField(Type)


class Student(Model):

    user = OneToOneField(User, on_delete=CASCADE, null=True)
    group_link = ManyToManyField(Group)
    name = CharField(max_length=60, null=True)
    group = CharField(max_length=10, null=True)
    practice = ManyToManyField(Practice)
    edu_profile = CharField(max_length=50, null=True)
    contract = BooleanField(default=False)
    degree = CharField(max_length=50, null=True)
    status = CharField(max_length=20, null=True)


class Diary(Model):
    student = ForeignKey(Student, on_delete=CASCADE)
    description = CharField(max_length=40, null=True)
    date = DateField
    practice = OneToOneField(Practice, null=True)



class Deanery(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    group = ManyToManyField(Group)


class Pass(Model):
    contract_number = IntegerField
    contract_date = DateField
    practice = OneToOneField(Practice)
    necessary_works = CharField(max_length=230, null=True)
    student = ForeignKey(Student)
    report = TextField(max_length=2140, null=True)
    review = TextField(max_length=1540, null=True)
    mark = CharField(max_length=20, null=True)


class Dates(Model):
    dateFrom = DateField
    dateTo = DateField
    practice = ForeignKey(Student, on_delete=CASCADE)


class IndividualTask(Model):
    student = ForeignKey(Student, on_delete=CASCADE, related_name='студент')
    dateFrom = DateField
    dateTo = DateField
    practice = ForeignKey(Student, on_delete=CASCADE, related_name='практика', null=True)
    task_number = IntegerField
