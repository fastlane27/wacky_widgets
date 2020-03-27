from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Sum
from .models import Widget
from .forms import WidgetForm


class WidgetList(ListView):
    model = Widget
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['widget_form'] = WidgetForm()
        total = Widget.objects.aggregate(Sum('quantity'))['quantity__sum']
        context['widget_quantity'] = total
        return context


def create_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('index')


def delete_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('index')
