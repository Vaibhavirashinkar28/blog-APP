from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
		title=models.CharField(max_length=50)
		sdesc=models.CharField(max_length=50)
		det=models.CharField(max_length=300)
		cat=models.IntegerField()
		active=models.IntegerField()
		is_deleted=models.CharField(max_length=5)
		dt=models.DateTimeField(default =datetime.now)
		uid=models.IntegerField()
		
		def __str__(self):


			return self.title