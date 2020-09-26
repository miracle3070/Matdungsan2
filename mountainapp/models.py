from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mountain(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    completed = models.ManyToManyField(User, related_name='complited', blank=True)
    image = models.ImageField(upload_to='images/', blank=True) # 사진
    latitude = models.FloatField(null = True) # 위도
    longtitude = models.FloatField(null = True) # 경도
    completed_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name