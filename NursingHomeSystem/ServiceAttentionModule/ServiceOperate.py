# -*- coding: utf-8 -*-

import datetime
from ManageModels.models import ServiceInfo, NursingItemInfo
from ServiceAttentionModule.RecordOperate import *


# 对客户的服务记录做增添、删除、续费、查找操作
class ServiceOperate(object):
    @staticmethod
    def add_service(service, operator_id):
        # 添加一条服务记录要将一位客户和一项护理项目的信息链接
        # 同时生成一条交易记录record
        if int(service.time) == 0:
            status = '欠费'
        elif int(service.time) <= 2:
            status = '即将用尽'
        else:
            status = '正常'

        ServiceInfo(clientID=Customer.objects.get(customerID=service.clientID),
                    itemID=NursingItemInfo.objects.get(itemID=service.itemID),
                    remaining=service.time,
                    status=status).save()
        # 将服务添加给客户后还要生成记录
        RecordOperate().add_service_record(service, operator_id)

    @staticmethod
    def renew(service, operator_id, quantity):
        # 对一项已经存在的服务续费,增加服务的剩余时间，生成交易记录，再更新一下服务的状态信息
        service_remaining = service.remaining + int(quantity)
        if service_remaining <= 2:
            service_status = '即将用尽'
        else:
            service_status = '正常'
        service.remaining = service_remaining
        service.status = service_status
        service.save()
        RecordOperate().add_renew_record(service, operator_id, quantity)

    @staticmethod
    def remove(service, operator_id):
        # 删除一项服务，并生成一条删除记录
        service.delete()
        RecordOperate.add_delete_record(service, operator_id)

    @staticmethod
    def search(client_id):
        # 查找某位客户的所有服务信息
        client = Customer.objects.get(customerID=client_id)
        return ServiceInfo.objects.filter(clientID=client)
