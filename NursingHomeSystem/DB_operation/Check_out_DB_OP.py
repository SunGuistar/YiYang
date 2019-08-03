
from django.db.models import  Q
from ManageModels.models import *

from ManageModels.models import *



class Check_out_DB_OP(object):
    @staticmethod
    def add(c_o):

        t1 = Check_out(customerID = c_o.customerID, check_out_type = c_o.check_out_type,
                          check_out_reason = c_o.check_out_reason,
                          check_out_time = c_o.check_out_time, remark = c_o.remark,
                          time = c_o.time, check_out_state = c_o.check_out_state)

        t1.save()
        return

    @staticmethod
    def search(dict):
        q = Q()

        if 'customerID' in dict:
            q = q&Q(customerID = dict['customerID'])
        if 'check_out_type' in dict:
            q = q&Q(check_out_type = dict['check_out_type'])
        if 'check_out_state' in dict:
            q = q & Q(check_out_state = dict['check_out_state'])

        check_out_list = Check_out.objects.filter(q)

        print(type(check_out_list))

        return check_out_list

    @staticmethod
    def remove(customerID):

        p0  = Check_out.objects.get(customerID = customerID)
        p0.delete()

        return True

    @staticmethod
    def modify(c_o):
        print("开始修改1！")
        print(c_o.customerID)
        p0 = Check_out.objects.get(customerID = c_o.customerID)

        p0.check_out_reason = c_o.check_out_reason
        p0.check_out_type = c_o.check_out_type
        p0.check_out_time = c_o.check_out_time
        p0.time = c_o.check_out_time
        p0.remark = c_o.remark
        print("修改成功！")
        p0.save()

        return  True

    @staticmethod
    def verify(customerID):
        # 退住审核申请通过
        p0 = Check_out.objects.get(customerID=customerID)

        p0.check_out_state = True

        # 客户状态改变

        p1 = Customer.objects.get(customerID=customerID)
        p1.state_2 = False
        # 床位状态改变

        p0.save()
        p1.save()

        return True
