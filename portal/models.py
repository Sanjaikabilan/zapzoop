from django.db import models
from django import forms
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.forms.fields import DateTimeField
from django.forms.widgets import DateTimeBaseInput, DateTimeInput
from django.utils.timezone import now


# Create your models here.










class Inform(models.Model):
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to='user/data/')
    created_at= models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title

