from django.db import models
import datetime

# Create your models here.
class DictWord(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)