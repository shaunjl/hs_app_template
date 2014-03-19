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
	resource_url=models.TextField(max_length=100,null=False, blank=True, default='',
		help_text="The WSDL Url for your web services- I.E. 'http://worldwater.byu.edu/interactive/dr/services/index.php/services/cuahsi_1_1.asmx?WSDL'"
	)
	resource_namespace=models.TextField(max_length=100,null=False, blank=True, default='',
		help_text='The namespace is probably {http://www.cuahsi.org/waterML/1.1/}'
	)
	class Meta:
		verbose_name = "Time Series"



