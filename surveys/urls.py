from django.conf.urls import url

from . import views as survey_views

urlpatterns = [
    url(
        r'(?P<survey_pk>\d+)/answer/$',
        survey_views.Answer.as_view(),
        name='answer'
    ),

    url(
        r'(?P<answer_pk>\d+)/show/$',
        survey_views.Show.as_view(),
        name='show',
    ),

]
