from django.db import models


class Alias(models.Model):
    alias = models.CharField(max_length=255)
    target = models.CharField(max_length=24)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)

    def __str__(self):
        return self.alias
