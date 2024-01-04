from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class CustomUser(AbstractUser):
    pass
    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # username = models.CharField(max_length=100, unique=True, verbose_name='username')
    # username = models.CharField(max_length=100, unique=True, primary_key=True, verbose_name='username')
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=256, unique=True, verbose_name='email')
    # date_joined = models.DateField(auto_now_add=True)
    # last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    # profile_image = models.ImageField(upload_to='images/profile', null=True)
    # biography = models.TextField(blank=True, null=True)
    # user_permissions = models.ManyToManyField(blank=True, verbose_name='user permissions')
    # interests = 
    # login_status = 

    def __str__(self):
        return self.username