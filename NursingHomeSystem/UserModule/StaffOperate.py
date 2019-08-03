# -*- coding: utf-8 -*-

from ManageModels.models import StaffInfo, UserInfo, StaffTypeInfo, PositionInfo
from UserModule.Staff import Staff
from django.db.models import Q
import datetime
import random


class StaffOperate(object):
    @staticmethod
    def add_to_db(staff):
        # 将一条Staff添加到数据库中，需要先检验Staff中的各个输入项是否合法
        # 将没有输入的项设为默认值，然后生成8位员工ID，其中1-4位是入职年份，5-6位是员工职位，7-10位随机生成
        # 然后生成员工的系统用户User，用户名为员工ID，密码默认为123456，用户类型为员工的职务，状态默认可用

        # 首先是根据出生日期生成年龄
        if staff.birthday == '':
            # 如果出生日期未填写则设为默认的出生日期
            staff.birthday = '1970-01-01'
        birthday = datetime.datetime.strptime(staff.birthday, '%Y-%m-%d')
        age = datetime.date.today().year - birthday.year

        # 然后员工的入职时间
        if staff.employeeDate == '':
            # 如果未填写入职时间，则默认今天的时间为入职时间
            staff.employeeDate = datetime.date.today().strftime('%Y-%m-%d')
        employee_date = datetime.datetime.strptime(staff.employeeDate, '%Y-%m-%d')

        # 最后生成员工的ID
        head_id = ''
        # 前4位根据入职年份
        head_id += str(employee_date.year)

        # 中间5-6位根据员工职位
        head_id += PositionInfo.objects.get(position=staff.position).positionID

        # 7-10位自动随机生成
        while True:
            i = 0
            tail_id = ''
            # 生成4位随机尾id
            while i < 4:
                tail_id += random.choice('0123456789')
                i += 1
            if len(StaffInfo.objects.filter(staffID=head_id+tail_id)) == 0:
                # 如果没有在员工表中查询到id相同的员工则可以使用这个id
                new_id = head_id + tail_id
                break

        # 然后将员工信息和用户信息分别录入两个表中
        user = UserInfo(username=new_id, password='123456', position=staff.position, status='未登录')
        user.save()
        StaffInfo(name=staff.name,
                  sex=staff.sex,
                  age=age,
                  birthday=birthday,
                  staffType=StaffTypeInfo.objects.get(staffType=staff.staffType),
                  employeeDate=employee_date,
                  position=PositionInfo.objects.get(position=staff.position),
                  jobTitle=staff.jobTitle,
                  phoneNumber=staff.phoneNumber,
                  introduction=staff.introduction,
                  remarks=staff.remarks,
                  staffID=new_id, user=user).save()

    @staticmethod
    def remove(staffs):
        for staff in staffs:
            staff.user.delete()
            staff.delete()

    @staticmethod
    def search(**arg_dic):
        # 查找的函数，目前包括的查询条件包括id、姓名、性别、员工类型（单）、职位（单）、
        # 职称（单）、手机号码（模糊）、年龄（精确）、年龄（范围）【未测试】
        q = Q()
        if 'staffID' in arg_dic and arg_dic['staffID'] != '':
            q = q & Q(staffID=arg_dic['staffID'])
        if 'name' in arg_dic and arg_dic['name'] != '':
            q = q & Q(name=arg_dic['name'])
        if 'sex' in arg_dic and arg_dic['sex'] != '':
            q = q & Q(sex=arg_dic['sex'])
        if 'staffType' in arg_dic and arg_dic['staffType'] != '':
            q = q & Q(category=arg_dic['staffType'])
        if 'position' in arg_dic and arg_dic['position'] != '':
            q = q & Q(position=arg_dic['position'])
        if 'jobTitle' in arg_dic and arg_dic['jobTitle'] != '':
            q = q & Q(jobTitle=arg_dic['jobTitle'])
        if 'phoneNumber' in arg_dic and arg_dic['phoneNumber'] != '':
            q = q & Q(phoneNumber__contains=arg_dic['phoneNumber'])
        if 'age' in arg_dic and arg_dic['age'] != '':
            q = q & Q(age=arg_dic['age'])
        if 'minAge' in arg_dic and arg_dic['minAge'] != '':
            q = q & Q(age__gte=arg_dic['minAge'])
        if 'maxAge' in arg_dic and arg_dic['maxAge'] != '':
            q = q & Q(age__lte=arg_dic['maxAge'])

        s_list = StaffInfo.objects.filter(q)
        return s_list

    @staticmethod
    def search_id(staff_id):
        return StaffInfo.objects.get(staffID=staff_id)

    @staticmethod
    def filter_search_id(staff_id):
        return StaffInfo.objects.filter(staff_id)

    @staticmethod
    def get_info(staff):
        return {'staffID': staff.staffID, 'name': staff.name, 'sex': staff.sex, 'birthday': staff.birthday,
                'age': staff.age, 'employeeDate': staff.employeeDate, 'position': staff.position,
                'jobTitle': staff.jobTitle, 'phoneNumber': staff.phoneNumber, 'introduction': staff.introduction,
                'remarks': staff.remarks}

    @staticmethod
    def modify(staffs, **arg_dic):
        for staff in staffs:
            if 'name' in arg_dic and arg_dic['name'] != '':
                staff.name = arg_dic['name']
            if 'sex' in arg_dic and arg_dic['sex'] != '':
                staff.sex = arg_dic['sex']
            if 'birthday' in arg_dic and arg_dic['birthday'] != '':
                staff.birthday = datetime.datetime.strptime(arg_dic['birthday'], '%Y-%m-%d')
                staff.age = datetime.date.today().year - staff.birthday.year
            if 'staffType' in arg_dic and arg_dic['staffType'] != '':
                new_type = StaffTypeInfo.objects.get(staffType=arg_dic['staffType'])
                staff.staffType = new_type
            if 'jobTitle' in arg_dic and arg_dic['jobTitle'] != '':
                staff.jobTitle = arg_dic['jobTitle']
            if 'employeeDate' in arg_dic and arg_dic['employeeDate'] != '':
                staff.employeeDate = datetime.datetime.strptime(arg_dic['employeeDate'], '%Y-%m-%d')
            if 'introduction' in arg_dic and arg_dic['introduction'] != '':
                staff.introduction = arg_dic['introduction']
            if 'remarks' in arg_dic and arg_dic['introduction'] != '':
                staff.remarks = arg_dic['remarks']

            staff.save()
            staff.user.save()







