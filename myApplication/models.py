from django.db import models

# Create your models here.
"""
In the blog/models.py file we define all objects called Models 
- this is a place in which we will define our blog post.
"""

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
"""
class is a special keyword that indicates that we are defining an object.
Post is the name of our model(Model la doi tuong). 
We can give it a different name (but we must avoid special characters and whitespaces). 
Always start a class name with an uppercase letter.
Always start a class name with an uppercase letter.

models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.        
"""

