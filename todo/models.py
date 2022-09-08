"""Todo app models"""
from django.db import models


class Bloglinks(models.Model):
    """ model for user input """
    user_name = models.CharField(max_length=70, null=False, blank=False)
    user_email = models.EmailField(max_length=35)
    user_done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.user_name
