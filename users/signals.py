# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import UserProfile

# @receiver(post_save, sender=UserProfile)
# def set_user_permissions(sender, instance, created, **kwargs):
#     """
#     Set user permissions based on their role
#     """
#     if created or kwargs.get('update_fields'):
#         # Get the user associated with this profile
#         user = instance.user
        
#         # Clear existing permissions
#         user.user_permissions.clear()
        
#         # Add permissions from the role
#         role_permissions = instance.role.permissions.all()
#         user.user_permissions.set(role_permissions)