from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Games(models.Model):
    name = models.CharField(max_length=200)
    date_updated = models.DateTimeField(default=timezone.now())
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
