import datetime
import random
from ManageModels.models import *


class Outgoing_Info(object):
    AppID = ''
    name = ''
    Cp_name = ''
    Cp_tel = ''
    Cp_rela = ''
    Remarks = ''
    wcsy=''
    Time_er = ''
    Time_eo = ''

    # 回院时间
    Time_ar = ''
    # 客户状态
    Ap_stat = False
    Ap_stat1 = False
    def __init__(self, name,Cp_name,Cp_tel,Cp_rela, Remarks,wcsy,Time_er ,Time_eo):
        # 各项属性的初始化
        self.name = name
        self.Cp_name = Cp_name
        self.Cp_tel = Cp_tel
        self.Cp_rela = Cp_rela
        self.Ap_stat = False
        self.Remarks = Remarks
        self.Time_er = Time_er
        self.Time_eo = Time_eo
        self.wcsy = wcsy

        self.Time_ar = ''
        self.Ap_stat1 = False

        new_app_id = datetime.date.today().strftime('%Y-%m-%d').replace('-', '')
        # 最后四位随机生成，若有重复则重新生成
        j = 0
        while j == 0:
            i = 0
            num = ''
            while i < 4:
                num += random.choice('0123456789')
                i += 1
            new_app_id += num
            res = AppInfo.objects.filter(AppID=new_app_id)

            if len(res) == 0:
                j = 1
            else:
                # 否则该条员工id无效，应当重新生成后四位员工id
                new_app_id -= num
                res.clear()
        self.AppID = new_app_id
