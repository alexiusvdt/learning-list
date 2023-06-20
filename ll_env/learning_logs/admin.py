from django.contrib import admin

# Register your models here.
from .models import Topic

# model managed thru the admin site
admin.site.register(Topic)
