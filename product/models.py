from django.db import models
from uuid import uuid4
from user.models import User

class Product(models.Model):

    class Meta:
        ordering = ['-updated_at']

    id = models.UUIDField(default=uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(null=False, blank=False)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    