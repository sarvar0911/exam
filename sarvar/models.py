from django.contrib.auth.models import User, Permission, Group
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.username


class About(AbstractBaseModel):
    title = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return f" {self.title} "


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
