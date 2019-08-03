# -*- coding: utf-8 -*-

from ManageModels.models import *
import random
from django.db.models import Q


class NursingTypeOperate(object):
    @staticmethod
    def add_to_db(nursing_type):
        # 在输入数据库前，检验护理项目名称是否合法，并生成一个2位数字ID

        # 获取所有已有的NursingTypeInfo表里的typeID
        res = NursingTypeInfo.objects.all()
        id_list = []
        for info in res:
            id_list.append(info.typeID)

        # 生成2位数字护理类型ID
        while 1:
            i = 0
            new_id = ''
            while i < 2:
                # 生成两位数ID
                new_id += random.choice('0123456789')
                i += 1
            if new_id not in id_list:
                # 如果new_id不在id_list中说明和已有id不重复，那么退出循环，new_id即是合法类型id
                # 否则重新生成ID
                break

        # 检验护理类型名称是否重复

        # 获取所有已有的护理类型名称
        name_list = []
        for info in res:
            name_list.append(info.name)

        # 检验类型名称是否重复，如果不重复则添加，重复就不添加到数据表里
        if nursing_type.name not in name_list:
            new_type = NursingTypeInfo(typeID=new_id, name=nursing_type.name, details=nursing_type.details)
            new_type.save()
            # 返回值为0，说明添加成功
            return '添加成功'
        else:
            # 返回值为1，则说明添加失败
            return '添加失败：重复的护理类型名称'

    @staticmethod
    def remove(nursing_types):
        for nursing_type in nursing_types:
            nursing_type.delete()

    @staticmethod
    def search(type_id='', type_name=''):
        q = Q()
        if type_id != '':
            q = q & Q(typeID=type_id)
        if type_name != '':
            q = q & Q(name=type_name)
        # 返回筛选后的列表
        return NursingTypeInfo.objects.filter(q)

    @staticmethod
    def modify(nursing_types, type_name='', type_details=''):
        for nursing_type in nursing_types:
            if type_name != '':
                nursing_type.name = type_name
            if type_details != '':
                nursing_type.details = type_details
            nursing_type.save()


