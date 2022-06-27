import uuid
from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    updated_at = models.DateTimeField('Updated at', auto_now=True, blank=False, null=False)
    created_at = models.DateTimeField('Created at', auto_now_add=True, blank=False, null=False)

    class Meta:
        abstract = True
