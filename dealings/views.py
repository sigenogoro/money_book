from django.shortcuts import render
from django.http import HttpResponse
from .models import Visualization
from .forms import MoneyForm
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView

# Create your views here.
def index(request):
    data = Visualization.objects.all()

    params = {
        'title': 'Money Index',
        'total_saving': 5000,
        'data': data,
        'data_list': change_list(data)
    }
    print(params)
    return render(request, 'dealings/index.html', params)

def create(request):
    if request.method == 'POST':
        money_add_info = Visualization()
        money_info = MoneyForm(request.POST, instance=money_add_info)
        money_info.save()
        return redirect(to='/dealings')
    params = {
        'title': 'Money Info',
        'form': MoneyForm()
    }
    return render(request, 'dealings/create.html', params)

def edit(request, num):
    get_model_value = Visualization.objects.get(id=num)
    if (request.method == 'POST'):
        money_info = MoneyForm(request.POST, instance = get_model_value)
        money_info.save()
        return redirect(to='/dealings')
    params = {
        'title': 'Hello',
        'id': num,
        'form': MoneyForm(instance = get_model_value)
    }
    return render(request, 'dealings/edit.html', params)

def delete(request, num):
    get_model_value = Visualization.objects.get(id=num)
    if request.method == 'POST':
        get_model_value.delete()
        return redirect(to='/dealings')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': get_model_value
    }
    return render(request, 'dealings/delete.html', params)

def change_list(data):
    a = [i.money for i in data]
    print(a)
    return a