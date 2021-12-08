from django.db import models
from django.db.models.base import ModelState
from django.db.models.enums import Choices


class Task(models.Model):
    TODO = "todo"
    DONE = "done"
    
    STATUS_CHOICES = (
        (TODO, "Todo"),
        (DONE, "Done")
    )
    
    description = models.CharField( max_length=255)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default = TODO);