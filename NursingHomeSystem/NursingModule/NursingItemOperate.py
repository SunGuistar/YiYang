# -*- coding: utf-8 -*-

from ManageModels.models import NursingItemInfo, NursingTypeInfo
import random
from django.db.models import Q


class NursingItemOperate(object):
    @staticmethod
    def add_to_db(nursing_item):
        # 将一个护理项目添加到数据库中，需要生成护理项目ID，检验项目名称、护理类型、护理价格（单价）是否合法

        # 先检验项目名称是否有冲突
        res = NursingItemInfo.objects.all()
        name_list = []
        for info in res:
            name_list.append(info.name)
        if nursing_item.name in name_list:
            # 如果有重复则返回1
            return 1

        # 检验护理类型是否存在
        res = NursingTypeInfo.objects.all()
        type_list = []
        for info in res:
            type_list.append(info.name)
        if nursing_item.itemType not in type_list:
            # 如果不存在则输入是不合法的
            return 1

        # 最后检验护理价格是否合法
        if int(nursing_item.price) < 0:
            # 价格不能为负数
            return 1

        # 检验输入合法后生成6位护理项目ID，包括前2位head_ID（由类型生成），后4位tail_ID（随机生成）
        name_id_dict = {}
        for info in res:
            name_id_dict[info.name] = info.typeID

        id_list = []
        res = NursingItemInfo.objects.all()
        for info in res:
            id_list.append(info.itemID)

        head_id = name_id_dict[nursing_item.itemType]

        # 生成后4位ID
        while 1:
            tail_id = ''
            i = 0
            while i < 4:
                tail_id += random.choice('0123456789')
                i += 1
            new_id = head_id + tail_id
            if new_id not in id_list:
                # 如果新的ID与已有护理项目ID不冲突则保存数据
                item = NursingItemInfo(itemID=new_id, name=nursing_item.name, price=nursing_item.price,
                                       addedService=nursing_item.addedService, details=nursing_item.details,
                                       status=nursing_item.status,
                                       itemType=NursingTypeInfo.objects.get(typeID=head_id))
                item.save()
                return 0

    @staticmethod
    def search(**arg_dict):
        q = Q()
        # 可选的参数有itemID，项目名称，价格范围（下限上限），是否增值服务，状态，itemType（护理类型名称）
        if 'item_id' in arg_dict and arg_dict['item_id'] != '':
            q = q & Q(itemID=arg_dict['item_id'])
        if 'name' in arg_dict and arg_dict['name'] != '':
            q = q & Q(name=arg_dict['name'])
        if 'min_price' in arg_dict and arg_dict['min_price'] != '':
            q = q & Q(price__gte=arg_dict['min_price'])
        if 'max_price' in arg_dict and arg_dict['max_price'] != '':
            q = q & Q(price__lte=arg_dict['max_price'])
        if 'added_service' in arg_dict and arg_dict['added_service'] != '':
            q = q & Q(addedService=arg_dict['added_service'])
        if 'details' in arg_dict and arg_dict['details'] != '':
            q = q & Q(details=arg_dict['details'])
        if 'status' in arg_dict and arg_dict['status'] != '':
            q = q & Q(status=arg_dict['status'])
        # 这里用到了外键 可能有问题【测试了能用】
        if 'item_type' in arg_dict and arg_dict['item_type'] != '':
            q = q & Q(itemType=arg_dict['item_type'].name)

        return NursingItemInfo.objects.filter(q)

    # 这个写完了还没测试过
    @staticmethod
    def remove(nursing_items):
        for nursing_item in nursing_items:
            nursing_item.delete()

    @staticmethod
    def modify(nursing_items, **arg_dict):
        # 可以更改的字段有护理名称name，价格price，增值服务，描述，状态，护理类型
        # 护理名称、价格、护理类型在更改之前要检验
        for nursing_item in nursing_items:
            if 'name' in arg_dict and arg_dict['name'] != '':
                # 在更改护理名称之前要先检验新的名称是否有冲突
                name_list = []
                res = NursingItemInfo.objects.all()
                for info in res:
                    name_list.append(info.name)
                if arg_dict['name'] in name_list:
                    # 说明有冲突，应该返回错误信息
                    return '姓名重复'
                else:
                    nursing_item.name = arg_dict['name']
            if 'price' in arg_dict and arg_dict['price'] != '' and arg_dict['price'] >= 0:
                nursing_item.price = arg_dict['price']
            # 检验布尔值是否有输入时的判定条件可能还需要更改
            if 'added_service' in arg_dict and arg_dict['added_service'] != '':
                nursing_item.addedService = arg_dict['added_service']
            if 'details' in arg_dict and arg_dict['details'] != '':
                nursing_item.details = arg_dict['details']
            if 'status' in arg_dict and arg_dict['status'] != '':
                nursing_item.status = arg_dict['status']
            if 'item_type' in arg_dict and arg_dict['item_type'] != '':
                # 检验护理项目类型是否存在于预设的护理类型表
                res = NursingTypeInfo.objects.all()
                type_list = []
                for info in res:
                    type_list.append(info.name)
                if arg_dict['item_type'] in type_list:
                    # 匹配说明是已录入的护理类型
                    nursing_item.itemType = NursingTypeInfo.objects.get(name=arg_dict['item_type'])
                else:
                    return '未查找到护理类型'
            nursing_item.save()
        return '修改完毕！'





