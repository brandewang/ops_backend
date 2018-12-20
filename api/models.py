from django.db import models
from django.core.exceptions import ValidationError
import hashlib

# Create your models here.


class AppGrp(models.Model):
    name = models.CharField(max_length=32, unique=True)
    describe = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField(max_length=32, unique=True)
    giturl = models.CharField(max_length=64)
    type = models.CharField(max_length=16)
    build = models.CharField(max_length=16)
    cover = models.BooleanField(default=False)
    monitor = models.BooleanField(default=False)
    group = models.ForeignKey(AppGrp, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    @property
    def group_name(self):
        return self.group.name



class User(models.Model):
    name = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=64, null=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.password = hashlib.md5((self.password + self.name).encode('utf-8')).hexdigest().upper()
        super(User, self).save(*args, **kwargs)