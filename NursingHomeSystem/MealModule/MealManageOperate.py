# -*- coding: utf-8 -*-

from ManageModels.models import MealStorageInfo, MealManageInfo, ClientInfo


class MealManageOperate(object):
    @staticmethod
    def add(meal_id, client_id, offer_day, offer_time, remarks):
        # 为一位客户添加一条制定膳食
        # mealID是前端根据选择的膳食条目发送给后端的，不用用户输入（来不及实现就手动输入）
        # 这里的mealID是mealID和参数相等的膳食仓库的对象
        # clientID是相应的客户信息对象
        meal = MealStorageInfo.objects.get(MealID=meal_id)
        client = ClientInfo.objects.get(ClientID=client_id)
        MealManageInfo(mealID=meal,
                       clientID=client,
                       offerDay=offer_day,
                       offerTime=offer_time,
                       remarks=remarks).save()

    @staticmethod
    def search(client_id=''):
        # 查找膳食管理信息，如果发送了客户ID则返回该客户的膳食管理信息
        # 如果没有发送客户ID可以返回所有客户ID的膳食管理信息
        return MealManageInfo.objects.filter(clientID=client_id)

    @staticmethod
    def remove(manage_ids):
        # 删除一条或多条膳食管理信息
        for info in manage_ids:
            info.delete()

    @staticmethod
    def modify(manage_id, **arg_dic):
        # 修改一条膳食管理信息
        manage = MealManageInfo.objects.get(id=manage_id)
        if 'meal_id' in arg_dic and arg_dic['meal_id'] != '':
            meal = MealStorageInfo.objects.get(mealID=arg_dic['meal_id'])
            manage.mealID = meal
        if 'client_id' in arg_dic and arg_dic['client_id'] != '':
            client = ClientInfo.objects.get(clientID=arg_dic['client_id'])
            manage.clientID = client
        if 'offer_day' in arg_dic and arg_dic['offer_day'] != '':
            manage.offerDay = arg_dic['offer_day']
        if 'offer_time' in arg_dic and arg_dic['offer_time'] != '':
            manage.offerTime = arg_dic['offer_time']
        if 'remarks' in arg_dic and arg_dic['remarks']:
            manage.remarks = arg_dic['offer_time']
        manage.save()

