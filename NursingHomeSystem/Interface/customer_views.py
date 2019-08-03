from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
# 自定义的类 和 数据库操作函数
from Classes.Check_in import Check_in_info
from DB_operation.Customer_DB_OP import *
from UserModule.StaffOperate import StaffOperate
import json
from ManageModels.models import Customer, Bed
from ServiceAttentionModule.ServiceOperate import ServiceOperate
# Create your views here.
# 与网页上的按钮一一对应，相当于响应函数


# 导航页
def customer_manage(request):
    return render(request, "Customer/main/CheckIn.html")

# 客户信息
def customer_info_html(request):
    return render(request, "Customer/info/CheckIn_xx.html")

def customer_info(request):
    print(request.POST)

    check_in_search_dict = dict()
    check_in_list = list()
    check_in_list1 = list()

    check_in_list = Customer_DB_OP.search(check_in_search_dict)

    for check_in in check_in_list:
        temp = dict()
        temp['customerID'] = check_in.customerID
        temp['name'] = check_in.name
        temp['sex'] = check_in.sex
        temp['age'] = check_in.age
        temp['nation'] = check_in.nation
        temp['nursing'] = check_in.nursing

        bed = Bed.objects.filter(CustomerId = temp['customerID'])
        if(bed.exists()):
            bed1=bed[0]
            temp['bedID'] = bed1.BedId
            print(temp['bedID'])
        else:
            temp['bedID'] = '-'
        if (check_in.state_1==True and check_in.state_2 == True):
            temp['state1'] = "在院"
        elif (check_in.state_1==False and check_in.state_2==True):
            temp['state1'] = "外出"
        elif (check_in.state_2==False):
            temp['state1'] = "退住"

        check_in_list1.append(temp)

    jsondata = json.dumps(check_in_list1)

    return HttpResponse(jsondata)



#详细信息
def customer_show_html(request):

    return render(request,'Customer/Detail/ShowInfo.html')

def customer_show(request):
    info = dict()
    check_in_list = list()
    check_in_list1 = list()
    if(request.POST):
        print(request.POST)
        info['customerID'] = request.POST['customerID']
        check_in_list = Customer_DB_OP.search(info)
        for check_in in check_in_list:
            temp = dict()
            temp['customerID'] = check_in.customerID
            temp['name'] = check_in.name
            temp['sex'] = check_in.sex
            check_in_list1.append(temp)

    jsondata = json.dumps(check_in_list1)
    return HttpResponse(jsondata)


def CheckIn_bl_sg_html(request):
    return render(request,'Customer/Detail/CheckIn_bl_sg.html')
def CheckIn_bl_sg(request):
    check_in_search_dict = dict()
    check_in_list = list()
    check_in_list1 = list()
    if (request.POST):
        check_in_search_dict['customerID'] = request.POST['customerID']

    check_in_list = Customer_DB_OP.search(check_in_search_dict)

    for check_in in check_in_list:
        temp = dict()

        temp['name'] = check_in.name
        temp['sex'] = check_in.sex
        temp['age'] = check_in.age
        temp['nation'] = check_in.nation
        temp['btype'] = check_in.btype

        temp['birthday'] = str(check_in.birthday)
        temp['ID_number'] = check_in.ID_number

        temp['province'] = check_in.province
        temp['city'] = check_in.city
        temp['area'] = check_in.area
        temp['address'] = check_in.address

        temp['marriage'] = check_in.marrige
        temp['type'] = check_in.type
        temp['height'] = check_in.height
        temp['weight'] = check_in.weight

        temp['phone_num1'] = check_in.phonenum1
        temp['phone_num2'] = check_in.phonenum2
        check_in_list1.append(temp)

    jsondata = json.dumps(check_in_list1)

    return HttpResponse(jsondata)


def BedInfo_html(request):
    return render(request,'Customer/Detail/BedsInfo.html')
def BedInfo(request):
    check_in_list1 = list()
    customer_id = request.POST['customerID']
    bed = Bed.objects.filter(CustomerId=customer_id)
    if(bed.exists()):
        bed = get_object_or_404(Bed, CustomerId=customer_id)
    temp = dict()
    temp['Building'] = '2'
    temp['floor'] = '2'
    temp['room'] = bed.Room.RoomId
    temp['bed'] = bed.BedId
    temp['time'] = '10'
    temp['cin_date'] = bed.BedStart
    temp['cout_date'] = bed.BedEnd
    temp['level'] = bed.BedState
    check_in_list1.append(temp)


    jsondata = json.dumps(check_in_list1)
    print(jsondata)
    return HttpResponse(jsondata)


def SetMeal_html(request):
    return render(request,'Customer/Detail/SetMeal.html')


def SetMeal(request):
    json_data = ''
    if request.POST:
        # 这里要等着和天志的设置服务对象合
        # 要通过发送来的客户ID获得该客户的护工ID，然后通过该护工ID来获得他的信息
        service = ServiceOperate.search(request.POST.get('customerID'))
        data_list = []
        for info in service:
            data = {'name': info.itemID.name,
                    'type': info.itemID.itemType,
                    'remaining': info.remaining,
                    'status': info.status}
            data_list.append(data)
        json_data = json.dumps(data_list)
    return HttpResponse()


def NersingWorker_Info_html(request):
    return render(request,'Customer/Detail/NersingWorker info.html')


def NersingWorker_Info(request):
    json_data = ''
    if request.POST:
        # 这里要等着和天志的设置服务对象合
        # 要通过发送来的客户ID获得该客户的护工ID，然后通过该护工ID来获得他的信息
        staff_id = '2019039602'
        staff_info = StaffOperate.search_id(staff_id)
        # 上面这两条是测试时写的，之后应该修改

        data_list = []
        data = {'name': staff_info.name,
                'sex': staff_info.sex,
                'age': staff_info.age,
                'type': staff_info.staffType.staffType,
                'cin_date': str(staff_info.employeeDate),
                'number': staff_info.staffID,
                'position': staff_info.position.position,
                'title': staff_info.jobTitle,
                'phone_num': staff_info.phoneNumber}
        data_list.append(data)
        json_data = json.dumps(data_list)
    return HttpResponse(json_data)



# 手工增加
def CheckIn_info_add_html(request):
    return render(request, "Customer/info_add/customer_info_add.html")
def CheckIn_info_add1_html(request):
    return render(request, "Customer/info_add/customer_info_add1.html")


def CheckIn_info_add1(request):

    return render(request, "Customer/info_add/customer_info_add1.html")


def CheckIn_info_add(request):
    print("11111")
    c=''
    if request.POST:
        print(request.POST)
        #注意birthday
        c_in = Check_in_info(name=request.POST['Name'],
                             sex=request.POST['Sex'],
                             age=request.POST['Age'],
                             nation=request.POST['Nation'],
                             ID_number=request.POST['ID_number'],
                             btype=request.POST['Btype'],
                             province=request.POST['Province'],
                             city=request.POST['City'],
                             area=request.POST['Area'],
                             address=request.POST['Address'],
                             marriage = request.POST['Marriage'],
                             type=request.POST['Type'],
                             height=request.POST['Height'],
                             weight=request.POST['Weight'],
                             phoneNum1= request.POST['Phone_num1'],
                             phoneNum2=request.POST['Phone_num2'],
                             remark=request.POST['remarks'],
                             birthday=request.POST.get('Birthday'),
                             )
        c=c_in.customerID
        Customer_DB_OP.add(c_in)
    print("打印一下ID")
    print(c)
    return HttpResponse(c)


# 删除
def Check_in_remove1(request):
    if request.POST:
        print(request.POST)
    Customer_DB_OP.remove(request.POST['id'])
    return HttpResponse("yes!")

def Check_in_remove2(request):
    rz_list = list()
    if request.POST:
        print(request.POST)

    for key in request.POST:
        if key == 'id[]':
            rz_list = request.POST.getlist(key)

    print (rz_list)
    for ID in rz_list:
        print(ID)
        Customer_DB_OP.remove(ID)
    return HttpResponse("yes!")

# 修改

def Check_in_modify(request):
    cin_modify_dict=dict()
    print("收到修改信息了")
    print(request.POST)
    cin_modify_dict['customerID'] = request.POST['customerID']
    cin_modify_dict['name'] = request.POST['name']
    cin_modify_dict['sex'] = request.POST['sex']
    cin_modify_dict['age'] = request.POST['age']
    cin_modify_dict['nation'] = request.POST['nation']
    cin_modify_dict['state'] = request.POST['state']

    Customer_DB_OP.modify(cin_modify_dict)
    return HttpResponse("yes")



# 简单条件查询  已实现
def search1(request):
    ctx = {}
    # 查询信息包装为字典
    customer_search1_dict = dict()
    if request.POST:
        if request.POST.get('condition1')!='':
            state = request.POST.get('condition1')
            if state == '在院' or '外出':
                customer_search1_dict['state1'] = state
            if state == '退住':
                customer_search1_dict['state2'] = state
        if request.POST.get('condition2')!='' and request.POST.get('info')!='':
            attr = request.POST.get('condition2')
            customer_search1_dict[attr] = request.POST.get('info')

    #抛给testdb中的函数去查询处理
    ctx['customer_list'] = Customer_DB_OP.search_test1(customer_search1_dict)
    return render(request, 'Customer_test/info_test.html', ctx)

# 复杂条件查询 还未实现


# 查看详细信息 已实现
def search3(request):
    ctx = {}
    customer_search3_dict = dict()
    #print("到这里了！") 测试
    if request.POST:
        if request.POST.get('customerID'):
            customer_search3_dict['customerID'] = request.POST.get('customerID')

    #print(customer_search3_dict) 测试

    ctx['customer_list'] = Customer_DB_OP.search_test3(customer_search3_dict)

    print('该返回了！')
    return render(request, 'Customer_test/customer_info_display_test.html',ctx)


# 单个删除，customerID 已实现
def remove1(request):

    if request.POST:
        if request.POST.get('customerID'):
            Customer_DB_OP.remove_test(request.POST.get('customerID'))

    print(request.POST.get('customerID'))
    return HttpResponse('删除成功！！！')

# 批量删除, customerID：[ID列表],还未实现
def remove2(request):
    customer_delete_set = set()
    if request.POST:
        if request.POST.get('customerID'):
            customer_delete_set = request.POST.get('customerID')

    print('接收到4月份枪毙名单啦！')
    print(request.POST.get('customerID'))

    return HttpResponse('删除成功！！！')



# 单个修改第一步
def modify(request):
    ctx = {}
    customer_search3_dict = dict()
    #print("到这里了！") 测试
    if request.POST:
        if request.POST.get('customerID'):
            customer_search3_dict['customerID'] = request.POST.get('customerID')

    ctx['customer_list'] = Customer_DB_OP.search_test3(customer_search3_dict)
    return render(request, 'Customer_test/customer_info_modify_test.html',ctx)

# 单个修改第二步
def modify1(request):
    customer_modify_dict = dict()
    if request.POST:
        # print(request.POST)
        customer_modify_dict.update(request.POST)
        for i in request.POST.keys():
            print(i,request.POST[i])
            customer_modify_dict[i] = request.POST[i]
        # 测试一下 POST的内容
        del customer_modify_dict['csrfmiddlewaretoken']
        for i in customer_modify_dict.keys():
            print(i,customer_modify_dict[i])

    Customer_DB_OP.modify_test(customer_modify_dict)

    return HttpResponse('修改成功！！！')

def login(request):
    return render(request,'Login/login.html')
def logout(request):
    #这里有一些操作！数据库的操作，将状态变一下

    return HttpResponse('Yes!')



def index_html(request):
    print(request.POST)
    return HttpResponse(request.POST)

def verify(request):

    if(request.POST.get('User')=='1234567890' and request.POST.get('Password')=='123'):
        print("成功了！")
        return HttpResponse("Yes")
    else:
        return HttpResponse("No1")


def rzbl(request):
    if(request.POST):
        print(request.POST)

    return HttpResponse("Yes")

