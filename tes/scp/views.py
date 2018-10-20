from django.shortcuts import render
import sqlite3
from scp import models
from .forms import AddForm


def home(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key']
            dictss = models.Information.objects.all().filter(title__contains=str(key))
            return render(request, 'home.html', locals())
    else:
        dicts = models.Information.objects.all()
        return render(request, 'home.html', locals())
