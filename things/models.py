from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator,MinValueValidator

class Thing(Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )
    description = models.CharField(
        max_length=100,
        blank = False
    )
    quantity = models.IntegerField(
        blank = False,
        validators=[MaxValueValidator(100),
                    MinValueValidator(0)]
        #test_quantity_must_not_be_greater_than_100,
        #test_quantity_must_not_be_negative
    )
