from django.db import models

# Create your models here.
class tour(models.Model):
    name = models.CharField(max_length=200)
    origin_country = models.CharField(max_length=200)
    destination_country = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.origin_country} to {self.destination_country} - ${self.price}"

