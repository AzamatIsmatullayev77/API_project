from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    Post=models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.title



