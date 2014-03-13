from mezzanine.pages.admin import PageAdmin
from django.contrib.gis import admin
from .models import tSRType #, tS

admin.site.register(tSRType, PageAdmin)
#admin.site.register(tS, PageAdmin)
