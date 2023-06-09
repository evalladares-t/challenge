from django.db import models

class BaseModelv1(models.Model):
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False)
    modified = models.DateTimeField(auto_now=True,
                                    editable=False)
    
    class Meta:
        abstract = True