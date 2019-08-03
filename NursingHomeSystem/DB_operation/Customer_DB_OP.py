from django.shortcuts import render
from django.views.decorators import csrf
from ManageModels.models import Customer

from django.db.models import Q
from ManageModels.models import *


class Customer_DB_OP(object):
    @staticmethod
    # 这里有25条
    def add(c):
        print("到这儿了！")
        print(c.marriage)
        t1 = Customer( customerID = c.customerID,
                       name = c.name,
                       sex = c.sex,
                       age = c.age,
                       nation =c.nation,
                       btype = c.btype,
                       ID_number = c.ID_number,
                       birthday = c.birthday,
                       province = c.province,
                       city = c.city,
                       area = c.area,
                       address = c.address,
                       marrige = c.marriage,
                       nursing = c.nursing,
                        type = c.type,
                        height = c.height,
                        weight =c.weight,
                        remark =c.remark,
                        phonenum1 = c.phoneNum1,
                        phonenum2 = c.phoneNum2,
                        check_in_date = c.check_in_date,
                        check_out_date = c.check_out_date,
                        state_1 = c.state1,
                        state_2 = c.state2,
                       )
        t1.save()
        return

    @staticmethod
    def search(dict):
        q = Q()

        if 'customerID' in dict:
            q = q & Q(customerID=dict['customerID'])
        if 'check_out_type' in dict:
            q = q & Q(check_out_type=dict['check_out_type'])

        check_in_list = Customer.objects.filter(q)

        return check_in_list

    @staticmethod
    def remove(id):

        p0 = Customer.objects.get(customerID=id)
        p0.delete()

    @staticmethod
    def modify(dict):
        p0 = Customer.objects.get(customerID=dict['customerID'])

        p0.name = dict['name']
        p0.sex = dict['sex']
        p0.age = dict['age']
        p0.nation = dict['nation']
        p0.state = dict['state']
        print("修改成功！")
        p0.save()

        return True

