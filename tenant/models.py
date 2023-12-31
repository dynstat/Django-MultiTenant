from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.core.validators import RegexValidator


class Client(TenantMixin):
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

    class Meta:
        unique_together = (
            "email",
            "phone_number",
        )

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Domain(DomainMixin):
    pass
