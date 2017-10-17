from django.views.generic import TemplateView

from surveys import models as surveys_models

class Top(TemplateView):
    template_name = "top.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "survey_list": surveys_models.Survey.objects.all(),
        })

        return context
