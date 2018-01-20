from django.db import models
from django.contrib.auth.models import User

class author(models.Model):
    name = models.ForeignKey(User,on_delete = models.CASCADE)
    details = models.TextField()
    author_image = models.FileField()

    def __str__(self):
        return self.name.username

class category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class articale(models.Model):
    article_author = models.ForeignKey(author,on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    articale_body = models.TextField()
    image = models.FileField()
    created_date = models.DateTimeField(auto_now = False, auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True, auto_now_add = False)
    category = models.ForeignKey(category,on_delete = models.CASCADE)

    def __str__(self):
        return self.title
