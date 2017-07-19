from django.db.models import Model, DateField, CharField, IntegerField, ForeignKey, ManyToManyField, OneToOneField, \
    CASCADE, TextField, BooleanField
from django.contrib.auth.models import User, Group


class Practice(Model):
    name = CharField(max_length=60, null=True)  # название практика
    teacher = CharField(max_length=60, null=True)  # руководитель от универа
    chief = CharField(max_length=100, null=True)  # руководитель от компании
    director = CharField(max_length=60, null=True)  # директор компании
    company = CharField(max_length=60, null=True)  # название организации
    address = CharField(max_length=60, null=True)  # адрес
    EDU = 'Учебная'
    PROD = 'Произведственная'
    DIP = 'Преддипломная'
    CHOICES = (
        (EDU, 'Учебная'),
        (PROD, 'Производственная'),
        (DIP, 'Преддипломная'))
    type = CharField(max_length=20,
                     choices=CHOICES,
                     default=EDU)
    date_from = DateField("Начало", null=True)
    date_to = DateField("Окончание", null=True)
    necessary_works = CharField(max_length=80, null=True)  # в каких видах работ нуждается

    def __str__(self):
        return self.name


class Student(Model):
    login = CharField(max_length=10, null=True)
    password = CharField(max_length=16, null=True)
    user = OneToOneField(User, on_delete=CASCADE, null=True)
    name = CharField(max_length=60, null=True)
    course = IntegerField(max_length=1, null=True)
    group = CharField(max_length=10, null=True)
    practice = ManyToManyField(Practice)
    engineering = '09.03.04 Программная инженерия'
    informatics = '09.03.03 Прикладная информатика'
    edu_profile = CharField(choices=(
        (engineering, '09.03.04 Программная инженерия'),
        (informatics, '09.03.03 Прикладная информатика')),
        max_length=50, null=True, default=engineering)  # направление
    contract = BooleanField(default=False)  # наличие договора
    status = CharField(max_length=20, null=True)  # бакалавр и тд.
    report = TextField(max_length=1429, null=True)  # big field 1
    review = TextField(max_length=1034, null=True)  # big field 2
    mark = CharField(max_length=20, null=True)  # оценка

    def __str__(self):
        return "%s - %s" % (self.name, self.group)

    def practice_view(self):
        str = ""
        practices = self.practice.all()
        for practice in practices:
            str += "%s, " % practice
        return str[:-2]


class Diary(Model):
    student = ForeignKey(Student, on_delete=CASCADE, null=True)
    practice = OneToOneField(Practice, null=True)


class DiaryRecord(Model):
    description = CharField(max_length=40, null=True)
    date = DateField('Дата', null=True)
    diary = ForeignKey(Diary, on_delete=CASCADE)
    number = IntegerField


class Deanery(Model):
    login = CharField(max_length=10, null=True)
    password = CharField(max_length=16, null=True)
    user = OneToOneField(User, on_delete=CASCADE)


class IndividualTask(Model):
    dateFrom = DateField(blank=True, null=True)
    dateTo = DateField(blank=True, null=True)
    desc = CharField(max_length=200, null=True)
    task_number = IntegerField
    student = ManyToManyField(Student)
    EDU = 'Учебная'
    PROD = 'Произведственная'
    DIP = 'Преддипломная'
    CHOICES = (
        (EDU, 'Учебная'),
        (PROD, 'Производственная'),
        (DIP, 'Преддипломная'))
    practice_type = CharField(max_length=20,
                              choices=CHOICES,
                              default=EDU)

    def __str__(self):
        return "%s - %s" % (self.desc, self.practice_type)
