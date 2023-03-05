from django.db import models
from django.contrib.auth.models import User
from products.models import Products


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='liked')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'product']
    
    def __str__(self):
        return f"{self.owner}'s like to {self.product}"
