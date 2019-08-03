import datetime
import random
from ManageModels.models import *


class Check_in_info(object):
    # 客户所有的信息
    # 新增页面需要展示的信息 19个
    name = ''
    sex = ''
    age = ''
    nation = ''
    ID_number = ''
    btype = ''
    birthday = ''
    province = ''
    city = ''
    area = ''
    address = ''
    marriage = ''
    nursing = ''
    type = ''
    height = ''
    weight = ''
    phoneNum1 = ''
    phoneNum2 = ''
    remark = ''

    # 自动生成的信息  6个
    customerID = ''
    check_in_date = ''
    state1 = True
    state2 = True

    bedID = ''  # 床位id选择床位后生成
    check_out_date = ''  # 退住审核通过后自动生成
    #注意birthday
    def __init__(self, name, sex, age, nation, ID_number,birthday,
                 btype, province,city,area,address,
                 marriage, type, height, weight,
                 phoneNum1,phoneNum2,remark):
        self.name = name
        self.sex = sex
        self.nation = nation
        self.ID_number = ID_number
        self.btype = btype
        self.birthday = birthday
        self.province = province
        self.city = city
        self.area = area
        self.address = address
        self.marriage = marriage

        self.type = type
        self.height = height
        self.weight = weight
        self.phoneNum1 = phoneNum1
        self.phoneNum2 = phoneNum2
        self.remark = remark
        self.age = age

        self.check_in_date = datetime.date.today().strftime('%Y-%m-%d')
        self.check_out_date = datetime.date.today().strftime('%Y-%m-%d')
        self.state1 = True
        self.state2 = True
        self.nursing = ''
        self.bedID = ''

        new_customer_id = datetime.date.today().strftime('%Y-%m-%d').replace('-', '')
        # 最后四位随机生成，若有重复则重新生成
        j = 0
        while j == 0:
            i = 0
            num = ''
            while i < 4:
                num += random.choice('0123456789')
                i += 1
            new_customer_id += num
            res = Customer.objects.filter(customerID=new_customer_id)

            if len(res) == 0:
                j = 1
            else:
                # 否则该条员工id无效，应当重新生成后四位员工id
                new_customer_id -= num
                res.clear()
        self.customerID = new_customer_id
