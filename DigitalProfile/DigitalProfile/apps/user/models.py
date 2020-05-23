from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self,email, password=None):
        if not email:
            raise ValueError('У пользователя должен быть e-mail')

        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using= self._db)
        return user
    
    def create_superuser(self,email, password):
        user = self.create_user(email,password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255,unique=True)
    surname = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128)
    birth_date = models.DateField(auto_now=True)
    phone_number = models.CharField(max_length=11)    
    vk_id= models.CharField(max_length=256)
    start_study_year = models.DateField(auto_now=True)
    end_study_year = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    

