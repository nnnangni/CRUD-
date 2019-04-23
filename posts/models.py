from django.db import models

# Create your models here.
class Facebook(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    facebook = models.ForeignKey(Facebook, on_delete=models.CASCADE)