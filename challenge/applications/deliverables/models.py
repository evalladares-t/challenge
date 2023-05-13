from django.db import models
from applications.v1.utils.BaseModel import BaseModelv1
from applications.packages.models import Package

# Create your models here.

class Deliverable(BaseModelv1):

    name = models.CharField(max_length=60)
    package = models.ForeignKey(Package,
                    related_name='deliverable_package',
                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Deliverable"
        verbose_name_plural = "Deliverables"