from mezzanine.pages.admin import PageAdmin
from django.contrib.gis import admin
from .models import TimeSeries

admin.site.register(TimeSeries, PageAdmin)

