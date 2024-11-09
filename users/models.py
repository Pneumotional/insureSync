# users/models.py
from django.contrib.auth.models import AbstractUser, Permission
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True) 

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.role})"

    def has_perm(self, perm, obj=None):
        if self.role and self.role.permissions.filter(codename=perm).exists():
            return True
        return super().has_perm(perm, obj)
