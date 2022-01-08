from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    # We do not need this table BUT we need these 2 fields in every other table
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name=_("Modified at"),
        auto_now=True
    )

    class Meta:
        abstract = True
