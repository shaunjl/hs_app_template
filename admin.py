from mezzanine.pages.admin import PageAdmin
from django.contrib.gis import admin
from .models import timeSeries

admin.site.register(timeSeries, PageAdmin)

