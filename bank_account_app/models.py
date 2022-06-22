from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# from .managers import UserManager

class Account(models.Model):
    pass

class User(AbstractUser):
    username = models.CharField(max_length=55, unique=True, null=False, blank=False)
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return 0


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_number = models.PositiveIntegerField(unique=True)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=12)

    def __str__(self):
        return str(self.account_number)


class TransferFunds(models.Model):
    sender = models.ForeignKey(UserAccount, related_name='outcome_transfers', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserAccount, related_name='income_transfers', on_delete=models.CASCADE)
    when = models.DateTimeField()
    total = models.FloatField()
    comment = models.CharField(max_length=255)

class Deposit(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    total = models.FloatField()
    bank_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    when = models.DateTimeField()

class Withdraw(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    total = models.FloatField()
    bank_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    when = models.DateTimeField()
