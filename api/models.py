from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import hashlib

# Create your models here.

TEAMS = ['FruitDay', 'OMS', 'TMS', 'SAP', 'PMS', 'GW']
TEAM_CHOICES = sorted((item, item) for item in TEAMS)
STATUS = ['success', 'failed']
STATUS_CHOICES = sorted((item, item) for item in STATUS)

class AppGrp(models.Model):
    name = models.CharField(max_length=32, unique=True)
    describe = models.CharField(max_length=64)
    team = models.CharField(choices=TEAM_CHOICES, default='FruitDay', max_length=32)

    def __str__(self):
        return self.name

    @property
    def app_name(self):
        return [{'id': i.id, 'name': i.name, } for i in self.app_set.all()]


class App(models.Model):
    name = models.CharField(max_length=32, unique=True)
    git_id = models.IntegerField(default=361)
    giturl = models.CharField(max_length=64)
    type = models.CharField(max_length=16)
    build = models.CharField(max_length=16)
    cover = models.BooleanField(default=False)
    monitor = models.BooleanField(default=False)
    group = models.ForeignKey(AppGrp, null=True, on_delete=models.SET_NULL)
    packing_lock = models.BooleanField(default=False)
    package_seq = models.IntegerField(default=0)

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


class Package(models.Model):
    tag = models.CharField(max_length=64, unique=True)
    committer = models.CharField(max_length=32, default='admin')
    create_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default='success')
    branch = models.CharField(max_length=16)
    short_id = models.CharField(max_length=16)
    env = models.CharField(max_length=16)
    package_path = models.CharField(max_length=256)
    log_path = models.CharField(max_length=256)
    app_id = models.ForeignKey(App, null=True, on_delete=models.SET_NULL)


