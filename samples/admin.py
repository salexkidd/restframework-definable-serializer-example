from django.contrib import admin
from definable_serializer.admin import DefinableSerializerAdmin

from . import models as samples_models

LIST_DISPLAY = (
    "id",
    "title",
)

LIST_DISPLAY_LINKS = (
    "id",
    "title",
)


@admin.register(samples_models.YAMLSample)
class YAMLSampleAdmin(DefinableSerializerAdmin):

    list_display = LIST_DISPLAY
    list_display_links = LIST_DISPLAY_LINKS


@admin.register(samples_models.JSONSample)
class JSONSampleAdmin(DefinableSerializerAdmin):

    list_display = LIST_DISPLAY
    list_display_links = LIST_DISPLAY_LINKS



@admin.register(samples_models.MultipleSample)
class MultipleSampleAdmin(DefinableSerializerAdmin):

    list_display = LIST_DISPLAY
    list_display_links = LIST_DISPLAY_LINKS
