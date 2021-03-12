from django.db import models
from account.models import Account

#from django.contrib.auth.models import Group

class Profile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='home/sergeybildin/Рабочий стол/DigitalProfile/DigitalProfile/DigitalProfile/static/media',height_field=None,blank=True, width_field=None, max_length=100, null=True)
    surname = models.CharField(verbose_name='Фамилия',max_length=100, null=True)
    name = models.CharField(verbose_name='Имя',max_length=100,null=True)
    patronymic = models.CharField(verbose_name='Отчество',max_length=100,null=True)
    MALE = 'Мужской'
    FEMALE = 'Мужской'
    SEX = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]
    sex = models.CharField(verbose_name='Пол',max_length=20,choices=SEX,default=MALE)
    phone_number = models.CharField(verbose_name='Номер телефона',max_length=12,null=True)
    birth_date = models.DateField(verbose_name='Дата рождения',auto_now=False,null=True)
    university = models.CharField(verbose_name='Университет',max_length=200,null=True)
    institute = models.CharField(verbose_name='Подразделение/факультет/институт',max_length=200,null=True)
    STUDENT = 'Студент'
    ORGANIZATOR = 'Организатор'
    ROLE = [
        (STUDENT, 'Студент'),
        (ORGANIZATOR, 'Организатор'),
    ]
    role = models.CharField(verbose_name='Роль',max_length=50,choices=ROLE,default=STUDENT)
    start_study_date = models.DateField(verbose_name='Дата начала обучения',auto_now=False, null=True)
    specialization = models.CharField(verbose_name='Напрвление/специальность',max_length=200, null=True)
    group = models.CharField(verbose_name='Номер группы',max_length=50, null=True)
    skills = models.TextField(verbose_name='навыки',max_length=300, null=True)
    skill_groups = models.ManyToManyField(
        'Groups', 
        through='Membership',
        through_fields=('person', 'group'),
        )
    def __str__(self):
        return self.surname + ' ' + self.name

    

class Groups(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        'Profile',        
        through='Membership',
        through_fields=('group', 'person'),
    )
    def __str__(self):
        return self.name

class Membership(models.Model):
    group = models.ForeignKey('Groups', on_delete=models.CASCADE)
    person = models.ForeignKey('Profile', on_delete=models.CASCADE)
    def __str__(self):
        return self.person.surname + ' ' + self.person.name + '->' + self.group.name
    
    
    
