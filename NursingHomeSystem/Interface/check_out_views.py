# Create your views here.

#django自带的
from django.http import  HttpResponse
from django.http import  HttpResponseRedirect
from django.shortcuts import render

#引入check_out 的类 需要自己写
from Classes.Check_out import *
# from Project.Self_test.Check_out_info import *
#引入check_out的数据库操作  需要自己写
from DB_operation.Check_out_DB_OP import *
import json

from django.core import serializers
from django.forms.models import model_to_dict


# 简单条件查询
# 简单条件查询
def search(request):
    ctx = {}
    check_out_search_dict = dict()
    check_out_list = list()
    check_out_list1 = list()
    if request.POST:
        if request.POST.get('customerID')!= '':
            check_out_search_dict['customerID'] = request.POST.get('customerID')
        if request.POST.get('check_out_type')!='':
            check_out_search_dict['check_out_type'] = request.POST.get('check_out_type')

    print(check_out_search_dict)
    ctx['check_out_list'] = Check_out_DB_OP.search(check_out_search_dict)
    #查询信息
    check_out_list = Check_out_DB_OP.search(check_out_search_dict)
    temp = dict()
    for check_out in check_out_list:
        print(type(check_out))
        temp['id'] = check_out.customerID
        temp['lx'] = check_out.check_out_type
        temp['reason'] = check_out.check_out_reason
        temp['ttime'] = str(check_out.check_out_time)
        temp['bz'] = check_out.remark
        temp['stime'] = str(check_out.time)
        temp['state'] = check_out.check_out_state
        check_out_list1.append(temp)
        print(check_out_list1)

    # temp = model_to_dict(check_out_list)
    # print(temp)

    jsondata = json.dumps(check_out_list1)
    print(jsondata)
    return render(request,'Check_out/check_out_1.html',ctx)

# 手工增加
def add1(request):
    if request.POST:
        # 包装成员一个对象
        c_o = Check_out_info(customerID=request.POST.get('customerID'),
                             check_out_type=request.POST.get('check_out_type'),
                             check_out_reason=request.POST.get('check_out_reason'),
                             check_out_time=request.POST.get('check_out_time'),
                             remark=request.POST.get('remark'))

        print(c_o.time)
        print(c_o.check_out_state)

        Check_out_DB_OP.add(c_o)
        return HttpResponse('添加成功！！！')

    return render(request,"Check_out/check_out_21.html")


# 批量增加，可以接受一个excel文件（或者zip文件）来进行处理。待实现
def add2(request):
    # for 循环 包装成对象 c_o
    # Check_out_DB_OP.add(c_o)
    if request.POST:
        return HttpResponse('批量增加处理成功！')
    return render(request,"Check_out/check_out_22.html")

# 单个修改
def modify1(request):
    print('hello')
    check_out_modify_dict = dict()
    if request.POST:
        check_out_modify_dict.update(request.POST)
        # 打印一下
        for i in request.POST.keys():
            print(i,request.POST[i])
            check_out_modify_dict[i] = request.POST[i]
        # 去掉字典中的特殊key-value
        del check_out_modify_dict['csrfmiddlewaretoken']
        for i in check_out_modify_dict.keys():
            print(i, request.POST[i])

        Check_out_DB_OP.modify(check_out_modify_dict)

        return HttpResponse('修改成功！')

# 批量修改,未实现，取出值循环调用单个修改即可
def modify2(request):
    return HttpResponse('批量修改成功！')

# 单个删除
def remove1(request):
    if request.POST:
        if request.POST.get('customerID'):
            Check_out_DB_OP.remove(request.POST.get('customerID'))
    return HttpResponse('删除成功！')

# 批量删除,未实现，取出值循环调用单个删除即可
def remove2(reqest):
    return HttpResponse('批量删除成功！')
# 单个审核

def verify1(request):
    if request.POST:
        if request.POST.get('customerID'):
            print(request.POST.get('customerID'))
            Check_out_DB_OP.verify(request.POST.get('customerID'))
    return HttpResponse('审核成功！')

# 批量审核，未实现。取出值循环调用单个审核即可
def verify2(request):
    return HttpResponse('批量审核成功！')



#姜莱兄

def tz1(request):
    return render(request,"Check_out/tz_xx.html")


def tz_xx(request):

    print(request.POST)

    check_out_search_dict = dict()
    check_out_list = list()
    check_out_list1 = list()

    print(check_out_search_dict)
    check_out_search_dict['check_out_state'] = False
    # 查询信息
    check_out_list = Check_out_DB_OP.search(check_out_search_dict)
    for check_out in check_out_list:
        temp = dict()
        #print(type(check_out))
        temp['id'] = check_out.customerID
        temp['lx'] = check_out.check_out_type
        temp['reason'] = check_out.check_out_reason
        temp['ttime'] = str(check_out.check_out_time)
        temp['bz'] = check_out.remark
        temp['stime'] = str(check_out.time)
        temp['state'] = check_out.check_out_state
        check_out_list1.append(temp)

    #print(check_out_list1)
    jsondata = json.dumps(check_out_list1)
   # print(jsondata)

    return HttpResponse(jsondata)


def tz_verify1(request):

    if request.POST:
        print("收到审核信息")
        print(request.POST)
        Check_out_DB_OP.verify(request.POST.get('id'))
    return HttpResponse()


def tz_remove1(request):

    if request.POST:
        print("收到删除信息")
        print(request.POST)
        Check_out_DB_OP.remove(request.POST.get('id'))
    return HttpResponse("收到删除信息")


def tz_verify2(request):
    tz_list = list()

    if request.POST:
        print("收到批量审核信息")
        print(request.POST)
    for key in request.POST:
        if key == 'id[]':
            tz_list = request.POST.getlist(key)
    print (tz_list)
    for ID in tz_list:
        print(ID)
        Check_out_DB_OP.verify(ID)
    return HttpResponse("收到批量审核信息")


def tz_remove2(request):
    tz_list = list()
    if request.POST:
        print("收到批量删除信息")
        print(request.POST)

    for key in request.POST:
        print("*****")
        print(key)
        if key == 'id[]':
            tz_list = request.POST.getlist(key)
        valuelist=request.POST.getlist(key)
        print(valuelist)
        print("*****")
    print("end")
    print (tz_list)
    for ID in tz_list:
        print(ID)
        Check_out_DB_OP.remove(ID)
    return HttpResponse("收到批量删除信息")


def tz_add1(request):
    if request.POST:
        # 包装成员一个对象
        print("发来对象了！")

        print(request.POST)
        customerID = request.POST.get('id');
        res = Customer.objects.filter(customerID=customerID)
        if len(res) == 0:
            print('该客户不存在！')
            return HttpResponse('该客户不存在！')
        else:
            c_o = Check_out_info(customerID=request.POST.get('id'),check_out_type=request.POST.get('lx'),
                        check_out_reason=request.POST.get('reason'),
                        check_out_time=request.POST.get('ttime'),
                        time=request.POST.get('stime'),
                        remark=request.POST.get('bz'))
        # print(request.POST.get('id'))
        # print(c_o.customerID)

            Check_out_DB_OP.add(c_o)

            return HttpResponse('添加成功！！！')

    return render(request,"Check_out/tz_bl_sg.html")

def tz_modify(request):
    if request.POST:
        print(request.POST)
        c_o = Check_out_info(customerID=request.POST.get('id'),
                             check_out_type=request.POST.get('lx'),
                             check_out_reason=request.POST.get('reason'),
                             check_out_time=request.POST.get('ttime'),
                             time=request.POST.get('stime'),
                             remark=request.POST.get('bz'))
        print("到这儿了！")
        Check_out_DB_OP.modify(c_o)
    return render(request,"Check_out/tz.html")



def tz(request):

    return render(request,"Check_out/tz.html")






