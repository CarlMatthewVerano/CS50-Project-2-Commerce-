from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.category}"

class AuctionListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    price = models.FloatField(max_length=64)
    createDate = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    imageURL = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    bidCtr = models.IntegerField(default=1)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name="categories")
    def __str__(self):
        return f"{self.title}"