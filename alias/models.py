from django.db import models


class Alias(models.Model):
    """
    Aliase holder

    Attributes:
        alias (str)
        target (str): slugs of other models/apps
        start (timestamp/datetime): microsecond precision 
        end (timestamp/datetime, None): microsecond precision
    """
    alias = models.CharField(max_length=255)
    target = models.CharField(max_length=24)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)

    def __str__(self):
        return self.alias
