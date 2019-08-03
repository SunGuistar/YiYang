# -*- coding: utf-8 -*-

from UserModule.UserOperate import UserOperate
from UserModule.StaffOperate import StaffOperate
from UserModule.Staff import Staff
from django.shortcuts import render


def add_staff(request):
    # 添加员工信息并创建用户
    ctx = {}
    if request.POST:

        new_staff = Staff(request.POST.get('name'),
                          request.POST.get('sex'),
                          request.POST.get('staffType'),
                          request.POST.get('position'),
                          request.POST.get('jobTitle'),
                          request.POST.get('phoneNumber'),
                          request.POST.get('birthday'),
                          request.POST.get('employeeDate'),
                          request.POST.get('introduction'),
                          request.POST.get('remarks'))
        StaffOperate.add_to_db(new_staff)
        ctx['msg'] = '操作完成！'
    return render(request, 'add_staff_info.html', ctx)


# 这下面是复制过来的
def search_info(request):
    ctx = {}
    if request.POST:
        op = StaffOperate()
        staff_list = op.search(staffID=request.POST.get('staffID'), name=request.POST.get('name'),
                               minAge=request.POST.get('minAge'), maxAge=request.POST.get('maxAge'),
                               age=request.POST.get('age'), sex=request.POST.get('sex'),
                               category=request.POST.get('category'),
                               position=request.POST.get('position'),
                               jobTitle=request.POST.get('jobTitle'),
                               phoneNumber=request.POST.get('phoneNumber'))
        ctx['staff_list'] = staff_list
    return render(request, 'search.html', ctx)


def remove_info(request):
    ctx = {}
    if request.POST:
        op = StaffOperate()
        staff_list = op.search(staffID=request.POST.get('staffID'), name=request.POST.get('name'),
                               minAge=request.POST.get('minAge'), maxAge=request.POST.get('maxAge'),
                               age=request.POST.get('age'), sex=request.POST.get('sex'),
                               category=request.POST.get('category'),
                               position=request.POST.get('position'),
                               jobTitle=request.POST.get('jobTitle'),
                               phoneNumber=request.POST.get('phoneNumber'))
        ctx['staff_list'] = staff_list
        op.remove(staff_list)
    return render(request, 'remove.html', ctx)


def modify_info(request):
    # 输入要修改的员工的ID，然后更改需要更改的属性
    if request.POST:
        op = StaffOperate()
        staff_list = op.search(staffID=request.POST.get('staffID'))
        StaffOperate.modify(staff_list,
                            name=request.POST.get('name'),
                            sex=request.POST.get('sex'),
                            birthday=request.POST.get('birthday'),
                            staffType=request.POST.get('staff_type'),
                            jobTitle=request.POST.get('job_title'),
                            employeeDate=request.POST.get('employee_date'),
                            introduction=request.POST.get('introduction'),
                            remarks=request.POST.get('introduction'))

