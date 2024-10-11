from django.db import models

# Create your models here.
class meals(models.Model):
    mealId = models.IntegerField()
    name = models.CharField(max_length=50)
    category = models.CharField (max_length=50)
    area = models.CharField(max_length=50)
    liked = models.BooleanField()
    def __str__(self):
        return self.name