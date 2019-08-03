# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ManageModels.models import *
from UserModule.StaffOperate import *
from UserModule.Staff import *
from ServiceAttentionModule.ServiceOperate import *
import json
from django.views.decorators.csrf import csrf_exempt
from NursingModule.NursingItemOperate import NursingItemOperate
from ServiceAttentionModule.Service import Service


def my_main(request):
    return render(request, 'user/main.html')


def welcome(request):
    return render(request, 'user/welcome.html')


def yghl(request):
    return render(request, 'user/yhgl.html')


def search(request):
    return render(request, 'user/search.html')


def yh_lr1(request):
    return render(request, 'user/yh_lr1.html')


def yh_lr2(request):
    return render(request, 'user/yh_lr2.html')


def yh_lr2_data(request):
    jason_data = ''
    data_list = list()
    if request.POST:
        staff_list = StaffOperate.search()
        for staff in staff_list:
            data_list.append({'name': staff.name,
                              'sex': staff.sex,
                              'age': staff.age,
                              'staffType': staff.staffType.staffType,
                              'employeeDate': str(staff.employeeDate),
                              'position': staff.position.position,
                              'jobTitle': staff.jobTitle,
                              'phoneNumber': staff.phoneNumber,
                              'ygh': staff.staffID,
                              'zh': str(staff.user.username)})

        jason_data = json.dumps(data_list)
    return HttpResponse(jason_data)


def yh_lr2_remove(request):
    if request.POST:
        staff_list = StaffOperate.search_id(request.POST.get('staffID'))
        staff_list.delete()
    return HttpResponse("已删除")


def yh_table(request):
    return render(request, 'user/yh_table.html')


def yh_table_data(request):
    if request.POST:

        new_staff = Staff(request.POST.get('name'),
                          request.POST.get('sex'),
                          request.POST.get('staffType'),
                          request.POST.get('position'),
                          request.POST.get('jobTitle'),
                          request.POST.get('phoneNumber'),
                          request.POST.get('birthday'),
                          request.POST.get('employeeDate'),
                          request.POST.get('introduction'),
                          request.POST.get('remarks'))
        StaffOperate.add_to_db(new_staff)
    return HttpResponse('信息已上传')


def yh_xx(request):
    print(request.POST)
    return render(request, 'user/yh_xx.html')


def yh_info_table(request):
    return render(request, 'user/yh_info_table.html')


@csrf_exempt
def yh_edit_table(request):
    return render(request, 'user/yh_edit_table.html')


@csrf_exempt
def yh_edit_table_data(request):
    json_data = ''
    if request.POST:
        print(request.POST.get('staff_id'))
        staff_info = StaffOperate.search_id(request.POST.get('staff_id'))
        data_list = []
        data = {'name': staff_info.name,
                'sex': staff_info.sex,
                'birthday': str(staff_info.birthday),
                'staffType': staff_info.staffType.staffType,
                'employeeDate': str(staff_info.employeeDate),
                'position': staff_info.position.position,
                'jobTitle': staff_info.jobTitle,
                'phoneNumber': staff_info.phoneNumber,
                'introduction': staff_info.introduction,
                'remarks': staff_info.remarks}
        data_list.append(data)
        json_data = json.dumps(data_list)
    return HttpResponse(json_data)


@csrf_exempt
def yh_edit_table_modify(request):
    json_data = ''
    if request.POST:
        print("进入修改函数")
        print(request.POST.get('name'),
              request.POST.get('sex'),
              request.POST.get('birthday'),
              request.POST.get('staffType'))
        print(request.POST.get('jobTitle'),
              request.POST.get('employeeDate'),
              request.POST.get('introduction'),
              request.POST.get('remarks'))
        op = StaffOperate()
        staff_list = op.search(staffID=request.POST.get('staffID'))
        StaffOperate.modify(staff_list,
                            name=request.POST.get('name'),
                            sex=request.POST.get('sex'),
                            birthday=request.POST.get('birthday'),
                            staffType=request.POST.get('staffType'),
                            jobTitle=request.POST.get('jobTitle'),
                            employeeDate=request.POST.get('employeeDate'),
                            introduction=request.POST.get('introduction'),
                            remarks=request.POST.get('remarks'))

    return HttpResponse(json_data)


# 服务关注
def khxxcx_data(request):
    jason_data = ''
    data_list = list()
    if request.POST:
        client_list = Customer.objects.all()
        for client in client_list:
            service_list = ServiceInfo.objects.filter(clientID=client)
            data_list.append({'khid': client.customerID,
                              'khname': client.name,
                              'hljb': client.nursing})
        jason_data = json.dumps(data_list)
    return HttpResponse(jason_data)


def khxxcx(request):
    return render(request, 'user/fwgz/khxxcx.html')


# 客户服务关注页面
def khfwgz(request):
    return render(request, 'user/fwgz/khfwgz.html')


@csrf_exempt
def khfwgz_data(request):
    jason_data = ''
    data_list = list()
    if request.POST:
        service_list = ServiceOperate.search(request.POST.get('client_id'))
        for service in service_list:
            data_list.append({'fwid': service.id,
                              'fwname': service.itemID.name,
                              'sysl': service.remaining,
                              'fwzt': service.status})
        jason_data = json.dumps(data_list)
    return HttpResponse(jason_data)


@csrf_exempt
def khfwgz_renew(request):
    if request.POST:
        service = ServiceInfo.objects.get(id=request.POST.get('id'))
        ServiceOperate().renew(service,
                               request.POST.get('operator_id'),
                               request.POST.get('quantity'))
    return HttpResponse()


@csrf_exempt
def khfwgz_delete(request):
    if request.POST:
        service = ServiceInfo.objects.get(id=request.POST.get('id'))
        ServiceOperate().remove(service, request.POST.get('operator_id'))
    return HttpResponse()


# 服务购买
def dxffgm(request):
    return render(request, 'user/fwgz/dxffgm.html')


def dxffgm_data(request):
    jason_data = ''
    data_list = list()
    if request.POST:
        info_list = NursingItemOperate.search()
        for info in info_list:
            data_list.append({'fwname': info.name,
                              'onejg': info.price,
                              'type': info.itemType.name})
        jason_data = json.dumps(data_list)
    return HttpResponse(jason_data)


def dxffgm_buy(request):
    jason_data = ''
    data_list = list()
    if request.POST:
        print(request.POST.get('item_name'))
        item = NursingItemInfo.objects.get(name=request.POST.get('item_name'))
        new_service = Service(client_id=request.POST.get('client_id'),
                              item_id=item.itemID,
                              time=request.POST.get('time'))
        ServiceOperate().add_service(new_service, request.POST.get('operator_id'))
    return HttpResponse()


# 交易记录
def jyjl(request):
    return render(request, 'user/fwgz/jyjl.html')


def jyjl_data(request):
    jason_data = ''
    data_list = list()
    if request.POST:
        record_list = RecordOperate.search(request.POST.get('client_id'))
        for record in record_list:
            data_list.append({'czlx': record.recordType,
                              'jynr': record.itemID.name,
                              'czje': record.amount,
                              'czz': record.operatorID.username,
                              'czsj': str(record.recordTime)})
        jason_data = json.dumps(data_list)
    return HttpResponse(jason_data)


# 服务详细信息
def xxxx(request):
    return render(request, 'user/fwgz/xxxx.html')


def xxxx2(request):
    return render(request, 'user/fwgz/xxxx2.html')


def xxxx_data(request):
    jason_data = ''
    data_list = list()
    if request.POST:
        if request.POST.get('service_id'):
            service = ServiceInfo.objects.get(id=request.POST.get('service_id'))
            item_id = service.itemID.itemID
            record_list = NursingItemOperate.search(item_id=item_id)
            for record in record_list:
                data_list.append({'xxms': record.details,
                                  'hllxid': record.itemType.typeID,
                                  'hllx': record.itemType.name,
                                  'hlxmmc': record.name,
                                  'hlxmid': record.itemID,
                                  'onejg': record.price,
                                  'xmqyzt': record.status,
                                  'zzfw': record.status})
        else:
            item_list = NursingItemOperate.search(name=request.POST.get('item_name'))
            for item in item_list:
                data_list.append({'xxms': item.details,
                                  'hllxid': item.itemType.typeID,
                                  'hllx': item.itemType.name,
                                  'hlxmmc': item.name,
                                  'hlxmid': item.itemID,
                                  'onejg': item.price,
                                  'xmqyzt': item.status,
                                  'zzfw': item.status})
        jason_data = json.dumps(data_list)
    return HttpResponse(jason_data)


# 服务初始化函数
def init_service(request):
    if request.POST:
        item_list = NursingItemInfo.objects.filter(addedService=False)
        print(request.POST.get('operator_id'))
        for item in item_list:
            print(request.POST.get('operator_id'))
            new_service = Service(client_id=request.POST.get('customer_id'),
                                  item_id=item.itemID,
                                  time=1)
            ServiceOperate().add_service(new_service, request.POST.get('operator_id'))
    return HttpResponse()
