from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    Post=models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    class RatingChoices(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RatingChoices, default=RatingChoices.ONE)

    def __str__(self):
        return f'{self.text} by {self.post}'


