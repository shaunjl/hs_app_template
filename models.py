from django.contrib.contenttypes import generic
from django.contrib.auth.models import User, Group
from django.db import models
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Ownable
from hs_core.models import AbstractResource
from hs_core.models import resource_processor
from mezzanine.pages.page_processors import processor_for

class TimeSeries(Page, RichText, AbstractResource):
    resource_description = models.TextField(null=False, blank=True, default='',
        help_text='I.E. Upper Provo River Flow',
    )
    resource_url=models.TextField(max_length=100,null=False, blank=True, default='',
        help_text="The WSDL Url for your web services- I.E. 'http://worldwater.byu.edu/interactive/dr/services/index.php/services/cuahsi_1_1.asmx?WSDL'"
    )
    resource_namespace=models.TextField(max_length=100,null=False, blank=True, default='',
        help_text='The namespace is probably {http://www.cuahsi.org/waterML/1.1/}'
    )
    resource_file=models.FileField(upload_to="timeseries",null=True,blank=True)
    class Meta:
        verbose_name = "Time Series"

processor_for(TimeSeries)(resource_processor)


