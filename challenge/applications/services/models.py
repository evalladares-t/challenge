from django.db import models
from applications.v1.utils.BaseModel import BaseModelv1

# Create your models here.

class Service(BaseModelv1):

    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return u'%s' % (self.name)

