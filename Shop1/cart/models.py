from django.db import models

class CartItem(models.Model):
    ItemId = models.IntegerField(unique=True)
    Amount = models.IntegerField()
    def __str__(self):
        return str(self.ItemId)