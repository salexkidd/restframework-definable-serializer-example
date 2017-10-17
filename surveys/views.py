from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from . import models as surveys_models


class Answer(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'answer.html'

    def get(self, request, survey_pk):
        survey = get_object_or_404(surveys_models.Survey, pk=survey_pk)
        serializer_class = survey.get_question_serializer_class()
        serializer = serializer_class()

        return Response({
            'serializer': serializer,
            'survey': survey,
        })

    def post(self, request, survey_pk):
        survey = get_object_or_404(surveys_models.Survey, pk=survey_pk)
        serializer_class = survey.get_question_serializer_class()
        serializer = serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'survey': survey})

        surveys_models.Answer.objects.create(
            survey=survey,
            respondent=request.user,
            answer=serializer.validated_data
        )

        return Response({
            'serializer': serializer,
            'survey': survey,
            'showing': True,
            'thankyou': True,
        })


class Show(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'answer.html'

    def get(self, request, answer_pk):
        answer = get_object_or_404(surveys_models.Answer, pk=answer_pk)
        survey = answer.survey

        serializer_class = survey.get_question_serializer_class()
        serializer = serializer_class(answer.answer)

        return Response({
            'serializer': serializer,
            'survey': survey,
            'showing': True,
        })
