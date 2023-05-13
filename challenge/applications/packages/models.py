from django.db import models
from django import forms
from applications.v1.utils.BaseModel import BaseModelv1
from applications.services.models import Service

# Create your models here.

'''

from django.contrib.postgres.fields import HStoreField
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField

class Deliverable(models.Model):
    id = models.BigAutoField()
    name = models.CharField(max_length=60)
    
    class Meta:
        abstract = True

class DeliverableForm(forms.ModelForm):
    id = models.BigAutoField()
    name = models.CharField(max_length=60)
    class Meta:
        model = Deliverable
        fields = (
            'id', 'name'
        )
'''
class Package(BaseModelv1):

    description = models.CharField(max_length=250,)
    price = models.FloatField(blank=True,
                                  default=0)
    service = models.ForeignKey(Service,
                    related_name='package_service',
                    on_delete=models.CASCADE)
    ##deliverables = ArrayField(DeliverableForm)

    class Meta:
        verbose_name = "Package"
        verbose_name_plural = "Packages"