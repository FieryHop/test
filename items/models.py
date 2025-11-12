from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name

# Create your models here.
