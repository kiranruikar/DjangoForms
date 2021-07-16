from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm


# Create your views here.


def index(request):
    form = SearchForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
        print(form.cleaned_data.get('name'))



    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('username'))
    # elif request.method == 'GET':
    #     print(request.GET)
    return render(request, 'index.html', {'form': form})
