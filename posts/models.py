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


class Post(models.Model):
    post_text = models.TextField()
    post_title = models.CharField(max_length=200)
    post_author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    pub_state = models.BooleanField(default=False)
    upd_date = models.DateTimeField("date updated")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Comment(models.Model):
    comment_text = models.TextField()
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.comment_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Like(models.Model):
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_status = models.BooleanField(default=True)
    like_author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.like_status


class Commend(models.Model):
    commend_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    commend_status = models.BooleanField(default=True)
    commend_author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.commend_status
