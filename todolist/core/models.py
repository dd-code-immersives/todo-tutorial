from django.db import models

# Create your models here.

# this will create a table in the database called todo with the fields
# name, status
class todo(models.Model):
    name = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
