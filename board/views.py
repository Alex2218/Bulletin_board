from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Bd, Rubric
from django.views.generic.edit import CreateView
from .forms import BdForm


def info(request):
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'board/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bd.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs, 'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'board/by_rubric.html', context)


class BdCreateView(CreateView):
    template_name = 'board/create.html'
    form_class = BdForm
    success_url = reverse_lazy('board:info')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
