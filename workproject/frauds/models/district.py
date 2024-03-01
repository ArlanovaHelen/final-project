from django.db import models


class District(models.Model):
    name = models.CharField(max_length=220)
    oblast = models.CharField(max_length=220)

    def __str__(self):
        return self.name
