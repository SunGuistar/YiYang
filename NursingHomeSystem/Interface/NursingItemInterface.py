# -*- coding: utf-8 -*-

from NursingModule.NursingItemOperate import NursingItemOperate
from NursingModule.NursingItem import NursingItem
from django.shortcuts import render


def add_nursing_item(request):
    # 添加一条护理项目
    ctx = {}
    if request.POST:
        new_item = NursingItem(name=request.POST.get('name'),
                               price=request.POST.get('price'),
                               added_service=request.POST.get('add_service'),
                               details=request.POST.get('details'),
                               status=request.POST.get('status'),
                               item_type=request.POST.get('item_type'))
        msg = NursingItemOperate().add_to_db(new_item)
        ctx['msg'] = msg
    return render(request, 'add_nursing_item.html', ctx)


def search_nursing_item(request):
    # 查找护理项目
    ctx = {}
    if request.POST:
        item_list = NursingItemOperate().search(item_id=request.POST.get('item_id'),
                                                name=request.POST.get('name'),
                                                min_price=request.POST.get('min_price'),
                                                max_price=request.POST.get('min_price'),
                                                added_service=request.POST.get('added_service'),
                                                details=request.POST.get('details'),
                                                status=request.POST.get('status'),
                                                item_type=request.POST.get('item_type'))
        ctx['item_list'] = item_list
    return render(request, 'search_nursing_item.html', ctx)


def remove_nursing_item(request):
    # 删除护理项目
    ctx = {}
    if request.POST:
        item_list = NursingItemOperate().search(item_id=request.POST.get('item_id'),
                                                name=request.POST.get('name'),
                                                min_price=request.POST.get('min_price'),
                                                max_price=request.POST.get('min_price'),
                                                added_service=request.POST.get('added_service'),
                                                details=request.POST.get('details'),
                                                status=request.POST.get('status'),
                                                item_type=request.POST.get('item_type'))
        ctx['num'] = len(item_list)
        NursingItemOperate().remove(item_list)
    return render(request, 'remove_nursing_item.html', ctx)


def modify_nursing_item(request):
    pass
