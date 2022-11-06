from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(max_length=50, upload_to="media/serviceee", blank=True, null=True)