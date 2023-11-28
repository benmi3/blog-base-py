import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=400)

    def __str__(self):
        return self.category_name


class Like(models.Model):
    vote = models.BooleanField(default=False)
    author = models.CharField(max_length=200)


class Post(models.Model):
    text = models.TextField()
    likes = models.IntegerFields(default=0)
    dislikes = models.IntegerField(default=0)
    author = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField("date published")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text
