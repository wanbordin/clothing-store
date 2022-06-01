from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from django.template import Template , Context
from django.template import RequestContext
import random
from clothing_store.models import *
# Create your views here.

def IndexPageStore(request):
    pd_list = Product_List.objects.all()
    data = dict()
    data['pd_list'] = pd_list
    return render(request, 'shop-template/index.html', data)
    
# def Category_List(request):
#     cr_shirt = Category_Shirt.objects.all()
#     data = dict()
#     data['cr_shirt'] = cr_shirt
#     # context ={}
#     # context['cr_shirt'] = Category_Shirt.objects.all()         
#     return render(request, 'shop-template/category.html', data)

def AboutPageStore(request):
    return render(request, 'shop-template/about-us.html')
    
def ContactPageStore(request):
    return render(request, 'shop-template/contact.html')

def DetailPageStore(request, id):
    pd_list = Product_List.objects.get(pk=id)
    return render(request, 'shop-template/detail.html', {'row': pd_list})
    
def EditPageStore(request, id):
    pd_list = Product_List.objects.get(pk=id)
    return render(request, 'shop-template/edit.html', {'row': pd_list})

# def UpdatePageStore(request, id):
#     pd_list = Product_List.objects.get(id=id)
#     form = Product_ListForm(request.POST or None, request.FILES, instance=pd_list)
#     if form.is_valid():
#         # file is saved
#         form.save()
#         return redirect('home_index_Store')
#     return render(request, 'shop-template/edit.html', {'row': form})
    