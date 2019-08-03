# -*- coding: utf-8 -*-

import datetime
from ManageModels.models import *


class RecordOperate(object):
    # 记录只能生成、查看，无法修改或删除
    @staticmethod
    def add_service_record(service, operator_id):
        # 用户新增一条服务的时候，要生成一条相应的交易记录
        record_time = datetime.datetime.now()
        record_type = '新增服务'
        # 新增服务的剩余时间即是交易数额
        quantity = service.time
        # 这里计算交易的金额，为数量*单价
        price = NursingItemInfo.objects.get(itemID=service.itemID).price
        amount = int(quantity) * price

        client_id = Customer.objects.get(customerID=service.clientID)
        operator = UserInfo.objects.get(username=operator_id)
        item_id = NursingItemInfo.objects.get(itemID=service.itemID)

        RecordInfo(recordTime=record_time,
                   recordType=record_type,
                   quantity=quantity,
                   amount=int(amount),
                   clientID=client_id,
                   operatorID=operator,
                   itemID=item_id).save()

    @staticmethod
    def add_renew_record(service_info, operator_id, quantity):
        # 用户对一项已存在的服务续费的时候，要生成一条对应的交易续费记录(不支持批量)
        record_time = datetime.datetime.now()
        record_type = '续费服务'
        record_quantity = quantity
        # 计算交易价钱
        price = NursingItemInfo.objects.get(itemID=service_info.itemID.itemID).price
        amount = int(record_quantity) * price

        client_id = Customer.objects.get(customerID=service_info.clientID.customerID)
        operator = UserInfo.objects.get(username=operator_id)
        item_id = NursingItemInfo.objects.get(itemID=service_info.itemID.itemID)

        RecordInfo(recordTime=record_time,
                   recordType=record_type,
                   quantity=record_quantity,
                   amount=amount,
                   clientID=client_id,
                   operatorID=operator,
                   itemID=item_id).save()

    @staticmethod
    def add_delete_record(service_info, operator_id):
        # 删除一项服务的时候需要生成删除记录
        # 这个还没测试过
        record_time = datetime.datetime.now()
        record_type = '删除服务'
        record_quantity = '0'
        amount = '0'
        client_id = Customer.objects.get(customerID=service_info.clientID.customerID)
        operator = UserInfo.objects.get(username=operator_id)
        item_id = NursingItemInfo.objects.get(itemID=service_info.itemID.itemID)

        RecordInfo(recordTime=record_time,
                   recordType=record_type,
                   quantity=record_quantity,
                   amount=amount,
                   clientID=client_id,
                   operatorID=operator,
                   itemID=item_id).save()

    @staticmethod
    def search(client_id):
        # 返回一位客户的所有交易记录
        # 这个也没有测试过
        client = Customer.objects.get(customerID=client_id)
        return RecordInfo.objects.filter(clientID=client)
