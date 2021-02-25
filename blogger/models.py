from django.db import models
from django.utils import timezone
# Create your models here.
# thumbail = models.ImageField(upload to="images")
class Article(models.Model):
    #STATUS_CHOICES = (
    #    ('d', 'Draft'),
    #    ('p', 'Published'),
    #)
    title = models.CharField(max_length=200)
    #slug = models.SlugField(max_length=100, unique= True)
    description = models.TextField()
    #publish = models.DateTimeField(default=timezone.now)
    #created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)
    #status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    author = models.CharField(max_length=50, default='alireza')
    def __str__(self):
        return self.title