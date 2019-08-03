# -*- coding: utf-8 -*-

import random
from ManageModels.models import MealStorageInfo
from django.db.models import Q


# 膳食仓库操作，用来操作养老院能够提供的膳食清单
class MealStorageOperate(object):
    @staticmethod
    def add(name, meal_type, label, price, image='', muslim=False, status=True):
        # 膳食ID自动生成
        while 1:
            meal_id = ''
            i = 0
            while i < 5:
                meal_id += random.choice('0123456789')
                i += 1
            if len(MealStorageInfo.objects.filter(mealID=meal_id)) == 0:
                break
        MealStorageInfo(mealID=meal_id,
                        name=name,
                        mealType=meal_type,
                        label=label,
                        price=price,
                        image=image,            # 这里可能会出错
                        muslim=muslim,
                        status=status).save()

    @staticmethod
    def search(**arg_dict):
        # 可以选择的筛选项有id，名称，种类，标签，价格（范围），清真，状态
        q = Q()
        if 'meal_id' in arg_dict and arg_dict['meal_id'] != '':
            q = q & Q(mealID=arg_dict['meal_id'])
        if 'name' in arg_dict and arg_dict['name'] != '':
            q = q & Q(name=arg_dict['name'])
        if 'meal_type' in arg_dict and arg_dict['meal_type'] != '':
            q = q & Q(meal_type=arg_dict['meal_type'])
        if 'label' in arg_dict and arg_dict['label'] != '':
            q = q & Q(label__contains=arg_dict['label'])
        if 'min_price' in arg_dict and arg_dict['min_price'] != '':
            q = q & Q(price__gte=arg_dict['min_price'])
        if 'max_price' in arg_dict and arg_dict['max_price'] != '':
            q = q & Q(price__lte=arg_dict['max_price'])
        if 'muslim' in arg_dict and arg_dict['muslim'] != '':
            q = q & Q(muslim=arg_dict['muslim'])
        if 'status' in arg_dict and arg_dict['status'] != '':
            q = q & Q(status=arg_dict['status'])

        return MealStorageInfo.objects.filter(q)

    @staticmethod
    def remove(storage_list):
        for storage in storage_list:
            storage.delete()

    @staticmethod
    def modify(meal_id, name='', meal_type='', label='', price='', image='', muslim=False, status=True):
        meal = MealStorageInfo.objects.get(mealID=meal_id)
        meal.name = name
        meal.mealType = meal_type
        meal.label = label
        meal.price = price
        meal.image = image
        meal.muslim = muslim
        meal.status = status
        meal.save()

