from django.db import models


class Education(models.Model):
    location_city = models.fields.CharField(max_length=100)