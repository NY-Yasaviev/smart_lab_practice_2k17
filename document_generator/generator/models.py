from django.db.models import Model, DateField, CharField, IntegerField, ForeignKey, ManyToManyField, OneToOneField, \
    CASCADE, TextField, BooleanField
from django.contrib.auth.models import User, Group


class Type(Model):
    EDU = 'EDU'
    PROD = 'PROD'
    DIP = 'DIP'
    CHOICES = (
        (EDU, 'Учебная'),
        (PROD, 'Производственная'),
        (DIP, 'Преддипломная'))
    name = CharField(max_length=20,
                     choices=CHOICES,
                     default=EDU)
    company = CharField(max_length=60, null=True)
    address = CharField(max_length=60, null=True)

    def __str__(self):
        return "%s , %s, %s" % (self.name, self.company, self.address)


class Practice(Model):
    name = CharField(max_length=60, null=True)
    teacher = CharField(max_length=60, null=True)
    director = CharField(max_length=60, null=True)
    type = ForeignKey(Type, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Student(Model):
    login = CharField(max_length=10, null=True)
    password = CharField(max_length=16, null=True)
    user = OneToOneField(User, on_delete=CASCADE, null=True)
    name = CharField(max_length=60, null=True)
    group = CharField(max_length=10, null=True)
    practice = ManyToManyField(Practice)
    edu_profile = CharField(max_length=50, null=True)
    contract = BooleanField(default=False)
    degree = CharField(max_length=50, null=True)
    status = CharField(max_length=20, null=True)

    def in_group(self, group):
        return Group.objects.get_by_natural_key(group) in self.user.groups


class Diary(Model):
    student = ForeignKey(Student, on_delete=CASCADE)
    description = CharField(max_length=40, null=True)
    date = DateField
    practice = OneToOneField(Practice, null=True)


class Deanery(Model):
    login = CharField(max_length=10, null=True)
    password = CharField(max_length=16, null=True)
    user = OneToOneField(User, on_delete=CASCADE)


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
