from django.db.models import Model, DateField, CharField, IntegerField, ForeignKey, ManyToManyField, OneToOneField, \
    CASCADE, TextField, BooleanField
from django.contrib.auth.models import User, Group


class Practice(Model):
    name = CharField(max_length=60, null=True)
    teacher = CharField(max_length=60, null=True)
    director = CharField(max_length=60, null=True)
    company = CharField(max_length=60, null=True)
    address = CharField(max_length=60, null=True)
    date_from = DateField
    date_to = DateField
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
    date_from = DateField("start", null=True)
    date_to = DateField("end", null=True)

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
    edu_profile = CharField(max_length=50, null=True)
    contract = BooleanField(default=False)
    degree = CharField(max_length=50, null=True)
    status = CharField(max_length=20, null=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.group)

    def practice_view(self):
        str = ""
        practices = self.practice.all()
        for practice in practices:
            str += "%s, " % practice
        return str[:-2]


class Diary(Model):
    student = ForeignKey(Student, on_delete=CASCADE)
    practice = OneToOneField(Practice, null=True)


class DiaryRecord(Model):
    description = CharField(max_length=40, null=True)
    date = DateField
    diary = ForeignKey(Diary, on_delete=CASCADE)


class Deanery(Model):
    login = CharField(max_length=10, null=True)
    password = CharField(max_length=16, null=True)
    user = OneToOneField(User, on_delete=CASCADE)


class Pass(Model):
    contract_number = IntegerField
    contract_date = DateField
    practice = OneToOneField(Practice)
    necessary_works = CharField(max_length=230, null=True)
    student = ForeignKey(Student, on_delete=CASCADE)
    report = TextField(max_length=2140, null=True)
    review = TextField(max_length=1540, null=True)
    mark = CharField(max_length=20, null=True)
    company_director = CharField(max_length=60, null=True)


class IndividualTaskDoc(Model):
    practice = OneToOneField(Practice, on_delete=CASCADE, null=True)
    student = ForeignKey(Student, on_delete=CASCADE)


class IndividualTask(Model):
    # student = ForeignKey(Student, on_delete=CASCADE, related_name='студент')
    dateFrom = DateField(null=True)
    dateTo = DateField(null=True)
    desc = CharField(max_length=200, null=True)
    task_number = IntegerField
    doc = ManyToManyField(IndividualTaskDoc)
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


class Report(Model):
    practice = OneToOneField(Practice, on_delete=CASCADE, null=True)
    student = ForeignKey(Student, on_delete=CASCADE)
