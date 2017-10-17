from django.db import models
from jsonfield.fields import JSONField

from definable_serializer.models import (
    DefinableSerializerByJSONField,
    DefinableSerializerByYAMLField,
    AbstractDefinitiveSerializerModel,
)


class YAMLSample(AbstractDefinitiveSerializerModel):
    title = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )
    sample_yaml = DefinableSerializerByYAMLField()


class JSONSample(AbstractDefinitiveSerializerModel):
    title = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )
    sample_json = DefinableSerializerByJSONField()


class MultipleSample(AbstractDefinitiveSerializerModel):
    title = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )
    sample_one = DefinableSerializerByYAMLField()
    sample_two = DefinableSerializerByJSONField()
