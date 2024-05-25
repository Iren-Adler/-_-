from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, RedirectView, FormView
from core import models, forms

from django.utils.timezone import now
import datetime

def index(request):
    return render(request, 'core/index.html')
# Create your views here.

class ClassBasedIndex(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["additional_info"] = now()
        return context


class AnimalList(ListView):
    model = models.Animal
    context_object_name = 'animals'
    template_name = 'core/animal_list.html'

class AnimalDetail(DetailView):
    model = models.Animal
    context_object_name = 'animal'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["additional_info"] = 'Режим работы зоопарка 10.00 - 19.30'
        return context

class Redirect(RedirectView):
    query_string = True
    url = 'http://paranoia.com/'

class SimpleForm(FormView):
    template_name = 'core/form.html'
    form_class = forms.SimpleForm
    success_url = '/index/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)