from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm


# Create your views here.


def index(request):
    form = SearchForm()
    return render(request, 'index.html', {'form': form})
