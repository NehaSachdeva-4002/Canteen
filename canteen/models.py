from django.db import models

class canteen(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.CharField(max_length=2083)
    
    def __str__(self):
         return self.name

class Order(models.Model):
    item = models.ForeignKey(canteen, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"