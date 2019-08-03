# -*- coding: utf-8 -*-

from MealModule.MealManageOperate import *
from ManageModels.models import MealManageInfo
from django.shortcuts import render


def add_meal_manage(request):
    ctx = {}
    if request.POST:
        MealManageOperate.add(request.POST.get('meal_id'),
                              request.POST.get('client_id'),
                              request.POST.get('offer_day'),
                              request.POST.get('offer_time'),
                              request.POST.get('remarks'))
    return render(request, 'add_meal_manage.html', ctx)


def search(request):
    ctx = {}
    if request.POST:
        ctx['info_list'] = MealManageOperate.search(request.POST.get('client_id'))
    return render(request, 'search_meal_manage.html', ctx)
