# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ManageModels.models import StaffTypeInfo, PositionInfo


def init_staff_position_type(request):
    # 为了方便测试，将员工职位和类型信息表初始化，以后可以增添对这两种信息的操作
    PositionInfo(positionID='00', position='管理员').save()
    PositionInfo(positionID='01', position='医生').save()
    PositionInfo(positionID='02', position='护士').save()
    PositionInfo(positionID='03', position='护工').save()

    StaffTypeInfo(typeID='00', staffType='固定工').save()
    StaffTypeInfo(typeID='01', staffType='合同工').save()
    StaffTypeInfo(typeID='02', staffType='代训工').save()
    StaffTypeInfo(typeID='03', staffType='临时工').save()
    StaffTypeInfo(typeID='04', staffType='实习生').save()

    return HttpResponse('初始化成功！')


def test(request):
    ctx = {}
    if request.POST:
        ctx['msg'] = '7777'
    return render(request, 'test.html')


def test2(request):
    ctx = {}
    if request.POST:
        if request.POST.get('msg') == '厉哥':
            ctx['msg'] = request.POST.get('msg')
            return render(request, 'test2.html', ctx)
        else:
            ctx['msg'] = '晓春'
            return render(request, 'test.html', ctx)


def my_main(request):
    return render(request, 'user/main.html')
