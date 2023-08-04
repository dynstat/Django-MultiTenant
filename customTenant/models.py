from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
            )
        ],
    )
