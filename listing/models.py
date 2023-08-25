from django.db import models
from accounts.models import Users
from datetime import datetime

# Create your models here.

class Properties(models.Model):
    agent_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    ptype = models.CharField(max_length=225)
    status = models.CharField(max_length=225)
    area = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    garage = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='post')
    price = models.FloatField()
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

