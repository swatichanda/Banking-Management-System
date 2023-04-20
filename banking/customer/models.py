from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    current_balance = models.FloatField(default=0)

class Transfer(models.Model):
    sender = models.ForeignKey(Customer, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Customer, related_name='receiver', on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
