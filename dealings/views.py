from django.shortcuts import render
from django.http import HttpResponse
from .models import Visualization, Income_visualization
from .forms import MoneyForm, IncomeForm
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView
import datetime
# Create your views here.
def index(request):
    data = Visualization.objects.all()
    income = Income_visualization.objects.all()

    params = {
        'day': datetime.datetime.today().strftime("%Y/%m/%d"),
        'total_saving': total(data, income),
        'data': change_dict(data),
        'income_data': change_dict2(income),
        'data_list': cost_list(data),
        'data_income': income_list(income)
    }
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


def income_create(request):
    if request.method == 'POST':
        income_add_info = Income_visualization()
        income_info = IncomeForm(request.POST, instance=income_add_info)
        income_info.save()
        return redirect(to='/dealings')
    params = {
        'title': 'Income Info',
        'form': IncomeForm()
    }
    return render(request, 'dealings/income_create.html', params)


def income_edit(request, num):
    get_model_value = Income_visualization.objects.get(id=num)
    if (request.method == 'POST'):
        money_info = IncomeForm(request.POST, instance = get_model_value)
        money_info.save()
        return redirect(to='/dealings')
    params = {
        'title': 'Hello',
        'id': num,
        'form': IncomeForm(instance = get_model_value)
    }
    return render(request, 'dealings/income_edit.html', params)


def income_delete(request, num):
    get_model_value = Income_visualization.objects.get(id=num)
    if request.method == 'POST':
        get_model_value.delete()
        return redirect(to='/dealings')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': get_model_value
    }
    return render(request, 'dealings/income_delete.html', params)


def change_dict(data):
    cost_dict = {}
    for cost_info in data:
        if cost_info.name in cost_dict:
            cost_dict[cost_info.name] += cost_info.money
        else:
            cost_dict[cost_info.name] = cost_info.money
    return cost_dict

def change_dict2(data):
    income_dict = {}
    for income_info in data:
        if income_info.name in income_dict:
            income_dict[income_info.name] += income_info.income
        else:
            income_dict[income_info.name] = income_info.income
    return income_dict



def cost_list(data):
    cost_dict = {}
    for cost_info in data:
        if cost_info.name in cost_dict:
            cost_dict[cost_info.name] += cost_info.money
        else:
            cost_dict[cost_info.name] = cost_info.money
    return list(cost_dict.values())


def income_list(income):
    income_dict = {}
    for income_info in income:
        if income_info.name in income_dict:
            income_dict[income_info.name] += income_info.income
        else:
            income_dict[income_info.name] = income_info.income
    return list(income_dict.values())


def total(data, income):
    income_sum = sum(income_list(income))
    cost_sum = sum(cost_list(data))

    total_saving = 70000 - (income_sum - cost_sum)
    return int(total_saving)
