from django.db import models
from django.contrib.auth.models import AbstractUser
# from .managers import UserManager

class Account(models.Model):
    pass

class User(AbstractUser):
    username = models.CharField(max_length=55, unique=True, null=False, blank=False)
    # objects = UserManager()

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
