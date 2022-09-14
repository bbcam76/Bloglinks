"""Todo app models"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Bloglinks(models.Model):
    """ model for user input """
    user_name = models.CharField(max_length=70, null=False, blank=False, default=None)
    user_email = models.EmailField(max_length=35, default=None)
    user_done = models.BooleanField(null=False, blank=False, default=False)
    title = models.CharField(max_length=200, null=False, blank=True, default=None)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(default=None)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True, default=None)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.title} by {self.user_name}"
