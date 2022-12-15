from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from uuid import uuid4

class CustomUserManager(UserManager):

    def _create_user(self, first_name, last_name, email, password, telephone, cpf, rg, **extra):

        if not email:
            raise ValueError('Prencha o e-mail')
        
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, telephone=telephone, cpf=cpf, rg=rg, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name=None, last_name=None, email=None, password=None, telephone=None, cpf=None, rg=None, **extra):
        extra.setdefault('is_superuser', True)
        extra.setdefault('is_staff', True)
        return self._create_user(first_name=first_name, last_name=last_name, email=email, password=password, telephone=telephone, cpf=cpf, rg=rg, **extra)
    
    def create_user(self, first_name=None, last_name=None, email=None, password=None, telephone=None, cpf=None, rg=None, **extra):
        extra.setdefault('is_superuser', False)
        extra.setdefault('is_staff', False)
        return self._create_user(first_name=first_name, last_name=last_name, email=email, password=password, telephone=telephone, cpf=cpf, rg=rg, **extra)

class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=255)   
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15, null=True, blank=True)
    rg = models.CharField(max_length=15, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'telephone']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name