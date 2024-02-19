from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='images/', blank=True)
	link = models.URLField(blank=True)
	def __str__(self):
		return self.title