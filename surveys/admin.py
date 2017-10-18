from django.contrib import admin
from definable_serializer.admin import DefinableSerializerAdmin

from . import models as surveys_models


@admin.register(surveys_models.Survey)
class SurveyAdmin(DefinableSerializerAdmin):

    list_display = (
        "id",
        "title",
    )

    list_display_links = (
        "id",
        "title",
    )


@admin.register(surveys_models.Answer)
class AnswerAdmin(DefinableSerializerAdmin):

    readonly_fields = (
        "create_at",
        "update_at",
    )

    list_display = (
        "id",
        "survey",
        "respondent",
        "create_at",
        "update_at",
    )

    list_display_links = (
        "id",
        "survey",
    )
