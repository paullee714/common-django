import uuid

from django.db import models


# Create your models here.
def uuid_string():
    return uuid.uuid4().hex


class BaseModel(models.Model):
    """
    Common Model Definition
        - uuid
        - created_at
        - updated_at
    """

    uuid = models.CharField(max_length=32, default=uuid_string, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
