from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    discount = models.SmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    likes=models.ManyToManyField(User,related_name='likes',blank=True)

    def __str__(self):
        return self.title

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product.title
class Comment(models.Model):
    class RatingChoices(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    massage = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comment_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='comment_product')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='comments/',null=True, blank=True)
    bad_comment = models.TextField(null=True, blank=True)
    good_comment = models.TextField(null=True, blank=True)
    rating_choices = models.IntegerField(choices=RatingChoices, default=RatingChoices.ONE)

    def __str__(self):
        return self.massage