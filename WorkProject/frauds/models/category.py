from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name