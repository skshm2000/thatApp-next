from django.db import models

class Account(models.Model):
    user_id = models.UUIDField(unique=True)
    name= models.CharField(max_length=100)
    number= models.CharField(max_length=10)
    knowledge_start_date = models.DateTimeField()
    knowledge_end_date = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=False)
