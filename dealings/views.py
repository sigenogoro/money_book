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
        'data': data
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

def make_chart(request):
    import django
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    datas = [20, 30, 10]
    labels = ['Wine', 'Sake', 'Beer']
    colors = ['yellow', 'red', 'green']
    # create figure
    fig = plt.figure(1,figsize=(4,4))
    ax = fig.add_subplot(111) 
    ax.axis("equal")
    pie = ax.pie(datas, #データ
                 startangle=90, #円グラフ開始軸を指定
                 labels=labels, #ラベル
                 autopct="%1.1f%%",#パーセント表示
                 colors=colors, #色指定
                 counterclock=False, #逆時計回り
                 )
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response