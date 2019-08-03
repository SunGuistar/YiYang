# -*- coding: utf-8 -*-


class Staff(object):
    name = ''
    sex = ''
    birthday = ''
    staffType = ''
    employeeDate = ''
    position = ''
    jobTitle = ''
    phoneNumber = ''
    introduction = ''
    remarks = ''

    def __init__(self, name, sex, staff_type, position,
                 job_title='', phone_number='', birthday='',
                 employee_date='', introduction='', remarks=''):
        # 各项属性的初始化
        self.name = name
        self.sex = sex
        self.staffType = staff_type
        self.position = position
        self.jobTitle = job_title
        self.phoneNumber = phone_number
        self.birthday = birthday
        self.employeeDate = employee_date
        self.introduction = introduction
        self.remarks = remarks
