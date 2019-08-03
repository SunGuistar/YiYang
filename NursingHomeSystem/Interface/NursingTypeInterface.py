# -*- coding: utf-8 -*-


from NursingModule.NursingType import NursingType
from NursingModule.NursingTypeOperate import NursingTypeOperate
from django.shortcuts import render
from django.http import HttpResponse


def add_nursing_type(request):
    # 添加护理类型
    ctx = {}
    if request.POST:
        new_type = NursingType(request.POST.get('name'), request.POST.get('details'))
        msg = NursingTypeOperate().add_to_db(new_type)
        ctx['msg'] = str(msg)
    return render(request, 'add_nursing_type.html', ctx)


def search_nursing_type(request):
    # 护理类型查找函数
    ctx = {}
    if request.POST:
        type_list = NursingTypeOperate().search(type_id=request.POST.get('type_id'),
                                                type_name=request.POST.get('name'))
        # 返回信息条数，和查询的数据列表
        ctx['num'] = len(type_list)
        ctx['type_list'] = type_list
    return render(request, 'search_nursing_type.html', ctx)


def remove_nursing_type(request):
    # 删除护理类型函数
    ctx = {}
    if request.POST:
        type_list = NursingTypeOperate().search(type_id=request.POST.get('type_id'),
                                                type_name=request.POST.get('name'))

        ctx['num'] = len(type_list)
        msg = NursingTypeOperate().remove(type_list)
        ctx['msg'] = msg
    return render(request, 'remove_nursing_type.html', ctx)


def modify_nursing_type(request):
    # 在同一页面修改护理类型的函数
    ctx = {}
    if request.POST:
        type_list = NursingTypeOperate().search(type_id=request.POST.get('type_id'),
                                                type_name=request.POST.get('name'))
        ctx['num'] = len(type_list)
        ctx['type_list'] = type_list
        NursingTypeOperate().modify(type_list, type_name=request.POST.get('name'),
                                    type_details=request.POST.get('details'))
    return render(request, 'modify_nursing_type.html', ctx)



