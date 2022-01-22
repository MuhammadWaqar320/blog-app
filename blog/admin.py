from django.contrib import admin
from .models import BlogComment
from .models import Post
# Register your models here.
admin.site.register((Post,BlogComment))