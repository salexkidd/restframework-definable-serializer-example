from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.exceptions import MethodNotAllowed, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    SessionAuthentication, TokenAuthentication
)

from . import models as surveys_models


class Answer(GenericAPIView):
    """
    Answer API
    """
    allowed_methods = ("GET", "POST", "OPTIONS",)
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,)
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    template_name = 'answer.html'

    def _get_previous_answer(self, survey):
        previous_answer = None
        try:
            previous_answer = surveys_models.Answer.objects.get(
                respondent=self.request.user, survey=survey)
        except surveys_models.Answer.DoesNotExist:
            pass

        return previous_answer

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        survey = get_object_or_404(
            surveys_models.Survey, pk=kwargs.get('survey_pk'))
        self.previous_answer = self._get_previous_answer(survey)
        self.survey = getattr(self.previous_answer, "survey", None) or survey

    def get_serializer_class(self, *args, **kwargs):
        return self.survey.get_question_serializer_class(*args, **kwargs)

    def get(self, request, survey_pk, format=None):
        response = None
        serializer = self.get_serializer()
        if self.previous_answer:
            serializer = self.get_serializer(data=self.previous_answer.answer)
            serializer.is_valid()

        if isinstance(self.request.accepted_renderer, TemplateHTMLRenderer):
            response = Response(
                {'serializer': serializer, 'survey': self.survey})
        else:
            if not self.previous_answer:
                raise NotFound()
            response = Response(serializer.data)

        return response

    def post(self, request, survey_pk):
        response = None
        serializer = self.get_serializer(data=self.request.data)

        if isinstance(self.request.accepted_renderer, TemplateHTMLRenderer):
            response = HttpResponseRedirect("/")
            if not serializer.is_valid():
                response = Response(
                    {'serializer': serializer, 'survey': self.survey})
            else:
                messages.add_message(
                    request, messages.SUCCESS, 'Thank you for posting! 💖')
        else:
            serializer.is_valid(raise_exception=True)
            response = Response(serializer.data)

        if serializer.is_valid():
            if self.previous_answer:
                self.previous_answer.answer = serializer.validated_data
                self.previous_answer.save()
            else:
                surveys_models.Answer.objects.create(
                    survey=self.survey,
                    respondent=request.user,
                    answer=serializer.validated_data
                )

        return response

    def options(self, request, *args, **kwargs):
        if request.accepted_media_type == TemplateHTMLRenderer.media_type:
            raise MethodNotAllowed(
                "It can not be used except when "
                "it is content-type: application/json."
            )
        return super().options(request, *args, **kwargs)
