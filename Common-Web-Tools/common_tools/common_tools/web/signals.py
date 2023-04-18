from django.db.models import signals
from django.dispatch import receiver

from common_tools.web.models import Profile

"""
Signals are used for:
1. Creating profile model for User
2. Send email after user register
    - Welcome email
    - Verification email
3. Setting `is_deleted` instead of actual delete
"""


@receiver(signals.pre_save, sender=Profile)
def profile_pre_created(instance, **kwargs):
    print(f"Pre create: {instance}")


@receiver(signals.post_save, sender=Profile)
def profile_post_created(instance, **kwargs):
    print(f"Post create: {instance}")
