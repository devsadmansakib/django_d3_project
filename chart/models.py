from django.db import models


# Create your models here.
class SampleData(models.Model):
    label = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.label
