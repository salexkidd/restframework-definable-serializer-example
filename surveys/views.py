from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.exceptions import MethodNotAllowed, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication
)

from . import models as surveys_models


class Answer(APIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,)
    template_name = 'answer.html'

    def get_previous_answer(self, survey):
        previous_answer = None
        try:
            previous_answer = surveys_models.Answer.objects.get(
                respondent=self.request.user,
                survey=survey
            )
        except surveys_models.Answer.DoesNotExist:
            ...

        return previous_answer

    def get(self, request, survey_pk, format=None):
        survey = get_object_or_404(surveys_models.Survey, pk=survey_pk)
        serializer_class = survey.get_question_serializer_class()

        # has Previous data?
        previous_answer = self.get_previous_answer(survey)

        serializer = serializer_class()
        if previous_answer:
            serializer = serializer_class(previous_answer.answer)

        response = None
        if isinstance(self.request.accepted_renderer, TemplateHTMLRenderer):
            response = Response({'serializer': serializer, 'survey': survey})
        else:
            if not previous_answer:
                raise NotFound()
            response = Response(serializer.data)

        return response

    def post(self, request, survey_pk):
        survey = get_object_or_404(surveys_models.Survey, pk=survey_pk)
        serializer_class = survey.get_question_serializer_class()
        serializer = serializer_class(data=request.data)

        response = None
        if isinstance(self.request.accepted_renderer, TemplateHTMLRenderer):
            response = HttpResponseRedirect("/")
            if not serializer.is_valid():
                response = Response({'serializer': serializer, 'survey': survey})
            else:
                messages.add_message(
                    request, messages.SUCCESS, 'Thank you for your posting! 💖')

        else:
            serializer.is_valid(raise_exception=True)
            response = Response(serializer.data)

        if serializer.is_valid():
            # has Previous data?
            previous_answer = self.get_previous_answer(survey)

            if previous_answer:
                previous_answer.answer = serializer.validated_data
                previous_answer.save()
            else:
                surveys_models.Answer.objects.create(
                    survey=survey,
                    respondent=request.user,
                    answer=serializer.validated_data
                )

        return response
