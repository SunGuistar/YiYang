
from django.db.models import  Q
from ManageModels.models import *

class Outgoing_DB_OP(object):
    @staticmethod
    def add(app):
        print("到这儿来 ")
        t1 = AppInfo( AppID=app.AppID, name=app.name, Time_eo=app.Time_eo, Time_er=app.Time_er,Time_ar=app.Time_ar,
                      Cp_tel=app.Cp_tel, Cp_rela=app.Cp_rela,Ap_stat=app.Ap_stat,Ap_stat1=app.Ap_stat1,
                      Cp_name=app.Cp_name,Remarks=app.Remarks, wcsy=app.wcsy)

        t1.save()
        return

    @staticmethod
    def search(dict):
        q = Q()

        if 'AppID' in dict:
            q = q&Q(AppID = dict['AppID'])
        if 'Ap_stat' in dict:
            q = q&Q(Ap_stat = dict['Ap_stat'])
        if 'Ap_stat1' in dict:
            q = q&Q(Ap_stat1 = dict['Ap_stat1'])

        outgoing_list = AppInfo.objects.filter(q)

        return outgoing_list

    @staticmethod
    def remove(name):

        p0  = AppInfo.objects.get(AppID =name)
        p0.delete()

        return True

    @staticmethod
    def modify1(dict):
        p0 = AppInfo.objects.get(AppID = dict['id'])
        p0.Time_ar = dict['backtime']
        p0.Ap_stat1 = 'True'
        id=p0.name
        p0.save()
        p1 = Customer.objects.get(customerID=id)
        print(p1.name)
        p1.state_1 = True
        p1.save()
        return True
    @staticmethod
    def modify2(ID,backtime):
        p0 = AppInfo.objects.get(AppID = ID)
        p0.Time_ar = backtime
        p0.Ap_stat1 = 'True'
        id=p0.name
        p0.save()
        p1 = Customer.objects.get(customerID = id)
        p1.state_1 = True
        p1.save()
        return True
    @staticmethod
    def modify(dict):
        p0 = AppInfo.objects.get(name = dict['id'])
        p0.wcsy = dict['wcsy']
        p0.Cp_name = dict['ptr']
        p0.Cp_rela = dict['lrgx']
        p0.Cp_tel = dict['dh']
        p0.Remarks = dict['bz']
        p0.Time_eo=dict['wctime']
        p0.Time_er=dict['yjtime']
    #    p0.Time_ar=dict['']
        p0.Ap_stat = dict['shstatus']
        p0.wcsy = dict['wcsy']
        p0.save()

        return True

    @staticmethod
    def verify(id):
        # 外出信息审核
        p0 = AppInfo.objects.get(AppID = id)
        p0.Ap_stat= 'True'
        id1 = p0.name
        p0.save()
        print("这里是")
        print(id1)
        print(type(id1))
        # 客户信息状态修改

        p1 = Customer.objects.get(customerID = id1)
        print(p1.name)
        p1.state_1 = False
        p1.save()

        return True