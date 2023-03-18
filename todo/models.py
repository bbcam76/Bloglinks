"""Todo app models"""
from django.db import models
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Bloglinks(models.Model):
    """ model for user input """
    user_name = models.CharField(max_length=150, null=False, blank=False, default=None) # noqa
    user_email = models.EmailField(max_length=35, default=None)
    user_done = models.BooleanField(null=False, blank=False, default=False)
    title = models.CharField(max_length=200, null=False, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(default=None)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.user_name}"


class Comment(models.Model):
    """ Comments model """
    post = models.ForeignKey(Bloglinks, on_delete=models.CASCADE, related_name="comments") # noqa
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
