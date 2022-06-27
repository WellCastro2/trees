import json

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from core.common.mixins import IsPlantedMixin
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.serializers import serialize


from core.models import PlantedTree
from core.forms import PlantedCreateForm


class Home(LoginRequiredMixin, TemplateView):
    """
        view initial page
    """
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context = {
            'planteds': self.request.user.get_planted_trees()
        }
        return context


class DetailTree(IsPlantedMixin, DetailView):
    """
        view to detail planted tree
    """

    template_name = 'tree/detail.html'
    model = PlantedTree


class ListAccountTree(LoginRequiredMixin, ListView):
    """
        view to list account planted tree
    """

    template_name = 'tree/list.html'
    model = PlantedTree

    def get_queryset(self):
        account_pk = self.kwargs.get("pk")
        queryset = PlantedTree.objects.filter(account=account_pk)
        return queryset


class PlantTreeView(LoginRequiredMixin, CreateView):
    """
        view to create/post new planted tree
    """
    template_name = 'tree/create.html'
    form_class = PlantedCreateForm
    success_url = "/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form(self):
        form = super(PlantTreeView, self).get_form()
        form.fields['account'].queryset = self.request.user.get_accounts()
        return form

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PlantTreeView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class JsonView(LoginRequiredMixin, TemplateView):
    """
        list all planted trees from logged user
    """
    def get(self, request):

        data = json.loads(serialize('json', request.user.get_planted_trees()))
        return JsonResponse(data, safe=False, content_type="application/json")
