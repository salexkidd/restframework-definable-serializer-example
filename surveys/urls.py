from django.conf.urls import url

from . import views as survey_views

app_name = "surveys"

urlpatterns = [
    url(
        r'(?P<survey_pk>\d+)/answer/$',
        survey_views.Answer.as_view(),
        name='answer'
    ),
]
