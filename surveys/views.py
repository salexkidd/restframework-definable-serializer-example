from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
try:
    from django.urls import resolve
except ModuleNotFoundError as e:
    from django.core.urlresolvers import resolve

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import MethodNotAllowed, NotFound
from rest_framework.renderers import TemplateHTMLRenderer

from . import models as surveys_models


from definable_serializer.contrib.pickup_serializer.viewsets import(
    PickupSerializerViewSet
)


class AnswerViewSet(PickupSerializerViewSet):
    template_name = 'answer.html'
    lookup_field = "survey__pk"
    queryset = surveys_models.Answer.objects.all()

    serializer_queryset = surveys_models.Survey.objects.all()
    serializer_field_name = "question"
    data_store_field_name = "answer"

    def get_api_name(self):
        definition_obj = self.get_serializer_define_object()
        return "Answer for {}".format(definition_obj.title)

    def get_unique_key_data(self):
        return {"respondent": self.request.user}

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(
            *args, **kwargs).filter(respondent=self.request.user)

    def retrieve(self, *args, **kwargs):
        if isinstance(self.request.accepted_renderer, TemplateHTMLRenderer):
            serializer = self.get_serializer()
            return Response({"serializer": serializer})

        response = super().retrieve(*args, **kwargs)
        return response

    def perform_create(self, serializer):
        # if not define obj, raise 404
        self.get_serializer_define_object()
        self.get_queryset().model.objects.create(
            respondent=self.request.user,
            survey=self.get_serializer_define_object(),
            **{self.data_store_field_name: serializer.validated_data}
        )

    def get_template_context(self):
        context = super().get_template_context()
        context["survey"] = self.get_serializer_define_object()
        return context
