from django.contrib.contenttypes import generic
from django.contrib.auth.models import User, Group
from django.db import models
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Ownable
from hs_core.models import AbstractResource

class tSRType(Page, RichText,AbstractResource): #tSRType = time series resource type 
        resource_description = models.TextField(null=False, blank=True, default='',
                help_text='I.E. Time Series',
        )

#class tS(Page, RichText, AbstractResource):  #tS = time series (object)
#	tsrtype = models.ForeignKey('tSRType')
#	resource_title = models.TextField('Time Series Title',max_length=60, help_text='Provide a searchable name for your Time Series')
#	resource_content = models.TextField(max_length = 200)



