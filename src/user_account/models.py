from django.contrib.auth.models import User
from django.db import models


class UserAccountProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = models.ImageField(default='pics/default.jpg', upload_to='pics')

    # Old signals implementation
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserAccountProfile.objects.create(user=instance)
