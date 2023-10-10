from django.db import models

class WeddingGuest(models.Model):
    name = models.CharField(max_length=255)
    attending = models.BooleanField(default=False)
    guests = models.PositiveIntegerField()

    def __str__(self):
        return self.name