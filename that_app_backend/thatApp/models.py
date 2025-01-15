from django.db import models
from uuid import uuid4


class Account(models.Model):
    user_id = models.UUIDField(
        unique=True, primary_key=True, default=uuid4, editable=False
    )
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10, unique=True)
    knowledge_start_date = models.DateTimeField(auto_now_add=True)
    knowledge_end_date = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=False)
