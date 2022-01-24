from django.db import models
from django.db.models import *
from django.contrib.auth.models import *
from django.utils.translation import gettext as _
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email_address, first_name, last_name, password=None, **other_fields):
        if email_address is None:
            raise ValueError('Email should not be null. Fill email field')
        
        email_address = self.normalize_email(email_address) #make it to lower case 

        user = self.model(username=username, email_address=email_address, first_name= first_name, last_name=last_name, password=password, **other_fields)
        user.set_password(password)
        user.save()

        return user
    
    #other fields here used for superuser properties
    def create_superuser(self, username, email_address, first_name, last_name, password=None, **other_fields):
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_staff',True)

        if other_fields.get('is_staff') is False:
            raise ValueError('Superuser should be a staff member, please enable it to True')

        if other_fields.get('is_superuser') is False:
            raise ValueError('Superuser should assigned is_superuser = True')
        
        return self.create_user(username, email_address, first_name, last_name, password, **other_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = CharField(max_length=20, unique=True)
    email_address = EmailField(_('email address'), unique=True)
    first_name = CharField(max_length=20, blank=True)
    last_name = CharField(max_length=20, blank=True)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    joined = models.DateField(default=timezone.now) 

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email_address'

    def __str__(self):
        return self.email_address

#python3 manage.py makemigrations app_name will actual make a migration folder for you