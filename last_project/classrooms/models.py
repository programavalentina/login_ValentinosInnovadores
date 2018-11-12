from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=1)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
