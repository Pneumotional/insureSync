# users/models.py
from django.contrib.auth.models import Permission, User, Group
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import Permission, Group
from django.db import models

# class Role(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     permissions = models.ManyToManyField(
#         Permission, 
#         blank=True,
#         related_name='roles'
#     )
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name

#     def add_permission(self, permission_codename, app_label='auth'):
#         """
#         Add a specific permission to the role
#         """
#         try:
#             permission = Permission.objects.get(
#                 codename=permission_codename, 
#                 content_type__app_label=app_label
#             )
#             self.permissions.add(permission)
#         except Permission.DoesNotExist:
#             print(f"Permission {permission_codename} not found")

#     def remove_permission(self, permission_codename, app_label='auth'):
#         """
#         Remove a specific permission from the role
#         """
#         try:
#             permission = Permission.objects.get(
#                 codename=permission_codename, 
#                 content_type__app_label=app_label
#             )
#             self.permissions.remove(permission)
#         except Permission.DoesNotExist:
#             print(f"Permission {permission_codename} not found")

#     def get_permissions(self):
#         """
#         Return a list of permission names for this role
#         """
#         return list(self.permissions.values_list('codename', flat=True))



# class CustomUser(AbstractUser):
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     role = models.ForeignKey(Role, on_delete=models.SET_NULL, related_name='role_permission', null=True, blank=True)

#     def __str__(self):
#         return f"{self.name} ({self.role})"

#     def has_perm(self, perm, obj=None):
#         if self.role and self.role.permissions.filter(codename=perm).exists():
#             return True
#         return super().has_perm(perm, obj)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    groups = models.ManyToManyField(
        Group, 
        related_name='user_profiles', 
        blank=True
    )


    

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})
