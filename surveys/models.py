from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from definable_serializer.models.compat import YAMLField

from definable_serializer.models import (
    DefinableSerializerByJSONField,
    DefinableSerializerByYAMLField,
    AbstractDefinitiveSerializerModel,
)


class Survey(AbstractDefinitiveSerializerModel):

    title = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=300,
        null=True,
        blank=True,
    )

    question = DefinableSerializerByYAMLField()

    custom_css = models.TextField(
        max_length=10000,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class Answer(models.Model):

    survey = models.ForeignKey("Survey")

    respondent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    answer = YAMLField(
        null=False,
        blank=False,
        default={},
        verbose_name="answer data",
        help_text="answer data"
    )

    create_at = models.DateTimeField(
        null=False,
        blank=False,
        auto_now_add=True,
        auto_now=False,
    )

    update_at = models.DateTimeField(
        null=False,
        blank=False,
        auto_now=True,
    )

    class Meta:
        unique_together = ("survey", "respondent",)
