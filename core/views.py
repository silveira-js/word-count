from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views import View

from .utils import word_counter
from .forms import TextForm


class TextView(FormView):
    form_class = TextForm
    template_name = "core/index.html"
    success_url = "/"

    def form_valid(self, form):
        text = form.cleaned_data['text']
        word_count = f'Word Count: {word_counter(text)}'
        context = self.get_context_data(form=form)
        context["counter"] = word_count
        return self.render_to_response(context)
