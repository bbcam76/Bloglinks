""" Admin file for bloglinks app """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Bloglinks, Comment


class BloglinksAdmin(SummernoteModelAdmin):
    """ Summernote admin class """

    summernote_fields = ('content')


admin.site.register(Bloglinks)
admin.site.register(Comment)
