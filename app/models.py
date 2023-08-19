from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    ORIENTATION_CHOICES = [
        ('landscape', 'Landscape'),
        ('portrait', 'Portrait'),
        ('square', 'Square'),
    ]

    DEFAULT_ORIENTATION = 'landscape'
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100,default='nature')
    tag = models.CharField(max_length=255,default='nature')
    location = models.CharField(max_length=255,default='Unknown')
    orientation = models.CharField(max_length=10, choices=ORIENTATION_CHOICES,default=DEFAULT_ORIENTATION)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
