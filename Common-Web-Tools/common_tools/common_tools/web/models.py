from django.db import models


class Profile(models.Model):
    email = models.EmailField()

    name = models.CharField(
        max_length=20,
    )

    # is_deleted = models.BooleanField(
    #     default=False,
    # )
