from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    image = models.ImageField(null=True, blank=True, max_length=255, upload_to='img/%y')
    address = models.CharField(max_length=1000000)
    dated = models.DateTimeField(default=datetime.now, blank=True)