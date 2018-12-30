from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>',views.delete, name='delete'),
    path('income_create', views.income_create, name ='income'),
    path('income_edit/<int:num>', views.income_edit, name='income_edit'),
    path('income_delete/<int:num>',views.income_delete, name='income_delete'),
]
