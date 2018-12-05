from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm

# Create your views here.
def index(request):
    params = {
        'title': 'Hello',
        'message': 'your data',
        'form': HelloForm()
    }
    if (request.method == 'POST'):
        params['message'] = 'ジャンル：' + '' + request.POST['name']
        params['form'] = HelloForm(request.POST)
    return render(request, 'dealings/index.html', params)