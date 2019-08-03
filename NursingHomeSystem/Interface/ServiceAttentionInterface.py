# -*- coding: utf-8 -*-

from ServiceAttentionModule.ServiceOperate import ServiceOperate
from ServiceAttentionModule.Service import Service
from ManageModels.models import NursingItemInfo, ServiceInfo
from django.shortcuts import render


def init_service_list(request):
    # 这个函数是客户初次选择服务套餐时，首先将默认的非增值服务添加进去
    # 浏览器要给服务器发送
    ctx = {}
    if request.POST:
        item_list = NursingItemInfo.objects.filter(addedService=False)
        for item in item_list:
            new_service = Service(client_id=request.POST.get('client_id'),
                                  item_id=item.itemID,
                                  time=request.POST.get('time'))
            ServiceOperate().add_service(new_service, request.POST.get('operator_id'))
    return render(request, 'init_service_list.html', ctx)


def add_service(request):
    # 添加一项服务，需要客户ID，服务ID和购买时长
    ctx = {}
    if request.POST:
        new_service = Service(client_id=request.POST.get('client_id'),
                              item_id=request.POST.get('item_id'),
                              time=request.POST.get('time'))
        ServiceOperate().add_service(new_service, request.POST.get('operator_id'))
    return render(request, 'add_service.html', ctx)


def renew_service(request):
    # 续费一项服务，需要客户ID，服务ID和续费时长
    # 浏览器发送给服务器续费的service的id，然后修改这条service的剩余时间
    ctx = {}
    if request.POST:
        service = ServiceInfo.objects.get(id=request.POST.get('id'))
        ServiceOperate().renew(service,
                               request.POST.get('operator_id'),
                               request.POST.get('quantity'))
    return render(request, 'renew_service.html', ctx)


def delete_service(request):
    # 删除一项服务，浏览器先发送过来一条service的id，然后删除
    ctx = {}
    if request.POST:
        service = ServiceInfo.objects.get(id=request.POST.get('id'))
        ServiceOperate().remove(service)
    return render(request, 'remove_service.html', ctx)


def show(request):
    # 返回一位客户所有的服务信息
    # 还没测试过
    ctx = {}
    if request.POST:
        service_list = ServiceOperate().search(request.POST.get('client_id'))
        ctx['service_list'] = service_list
    return render(request, 'show_service.html', ctx)

