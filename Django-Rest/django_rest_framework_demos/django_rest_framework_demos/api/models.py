from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    NAME_MAX_LENGTH = 25

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    NAME_MAX_LENGTH = 24
    PRICE_MIN_VALUE = 0.01

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
