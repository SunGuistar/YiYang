from django.http import  HttpResponse
from django.shortcuts import render, get_object_or_404

#引入check_out 的类 需要自己写
from Classes.Outgoing import *
from DB_operation.Outgoing_DB_OP import *
#引入check_out的数据库操作  需要自己写
import json
from django.core import serializers
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from ManageModels.models import *
from UserModule.StaffOperate import *
from UserModule.Staff import *
from ServiceAttentionModule.ServiceOperate import *
from django.views.decorators.csrf import csrf_exempt
from NursingModule.NursingItemOperate import NursingItemOperate
from ServiceAttentionModule.Service import Service





#导航页
def wc(request):
    return render(request,"Outgoing/wc.html")

#信息页
def wc_xx_html(request):
    return render(request,"Outgoing/wc_xx.html")

def wc_xx(request):

    print(request.POST)
    outgoing_search_dict = dict()
    outgoing_search_dict['Ap_stat1'] = "False"
    outgoing_list = list()
    outgoing_list1 = list()

    print(outgoing_search_dict)
    # 查询信息
    outgoing_list = Outgoing_DB_OP.search(outgoing_search_dict)
    for outgoing in outgoing_list:
        temp = dict()
        #print(type(outgoing_list))
        temp['id'] = outgoing.AppID
        temp['wcsy'] = outgoing.wcsy
        temp['wctime'] = str(outgoing.Time_eo)
        temp['yjtime'] = str(outgoing.Time_er)
        temp['ptr'] = outgoing.Cp_name
        temp['lrgx'] = outgoing.Cp_rela
        temp['dh'] = outgoing.Cp_tel
        temp['bz'] = outgoing.Remarks
        temp['shstatus'] = outgoing.Ap_stat
        outgoing_list1.append(temp)

    jsondata = json.dumps(outgoing_list1)
    print("答应")
    print(jsondata)
    return HttpResponse(jsondata)

# 审核
def wc_verify1(request):
    print('hello')
    if request.POST:

        print(request.POST)

        Outgoing_DB_OP.verify(request.POST.get('id'))

    return HttpResponse("收到审核信息")

def wc_verify2(request):
    wc_list = list()

    if request.POST:
        print("收到批量审核信息")
        print(request.POST)
    for key in request.POST:
        if key == 'id[]':
            wc_list = request.POST.getlist(key)
    print (wc_list)
    for AppID in wc_list:
        print(AppID)
        Outgoing_DB_OP.verify(AppID)
    return HttpResponse("收到批量审核信息")

#其他
def wc_hydj1(request):
    print('hello')
    outgoing_modify_dict = dict()
    if request.POST:
        outgoing_modify_dict.update(request.POST)
        # 打印一下
        for i in request.POST.keys():
            print(i,request.POST[i])
            outgoing_modify_dict[i] = request.POST[i]
        # 去掉字典中的特殊key-value
        Outgoing_DB_OP.modify1(outgoing_modify_dict)
        return HttpResponse('修改成功！')
def wc_hydj2(request):
    wc_list = list()
    if request.POST:
        print("收到批量回院信息")
        print(request.POST)
    wc_list = request.POST.getlist('id[]')
    backtime = request.POST.getlist('backtime')[0]
    print (wc_list)
    for ID in wc_list:
        print(ID)
        Outgoing_DB_OP.modify2(ID, backtime)
    return HttpResponse("修改成功")
#修改
def modify1(request):
    print('hello')
    outgoing_modify_dict = dict()
    if request.POST:
        outgoing_modify_dict.update(request.POST)
        # 打印一下
        for i in request.POST.keys():
            print(i,request.POST[i])
            outgoing_modify_dict[i] = request.POST[i]
        # 去掉字典中的特殊key-value
        Outgoing_DB_OP.modify(outgoing_modify_dict)

        return HttpResponse('修改成功！')
#删除
def wc_remove1(request):
    if request.POST:
        print("收到删除信息")
        print(request.POST)
        Outgoing_DB_OP.remove(request.POST.get('id'))
    return HttpResponse("收到删除信息")

def wc_remove2(request):
    wc_list = list()
    if request.POST:
        print("收到批量删除信息")
        print(request.POST)

    for key in request.POST:
        print("*****")
        print(key)
        if key == 'id[]':
            wc_list = request.POST.getlist(key)
        valuelist=request.POST.getlist(key)
        print(valuelist)
        print("*****")
    print("end")
    print (wc_list)
    for ID in wc_list:
        print(ID)
        Outgoing_DB_OP.remove(ID)
    return HttpResponse("收到批量删除信息")

def wc_add1(request):
    if request.POST:
        # 包装成员一个对象
        print("外出发来对象了！")
        print(request.POST)
        customerID = request.POST.get('id');
        res = Customer.objects.filter(customerID=customerID)
        if len(res) == 0:
            print('该客户不存在！')
            return HttpResponse('该客户不存在！')
        else:
            c_o = Outgoing_Info(name=request.POST.get('id'),
                        Time_eo=request.POST.get('wctime'),Time_er=request.POST.get('yjtime'),
                        Cp_name=request.POST.get('ptr'),Cp_rela=request.POST.get('lrgx'),Cp_tel=request.POST.get('dh'),
                        Remarks=request.POST.get('bz'),wcsy=request.POST.get('wcsy'))

            print(c_o.Time_ar)
            Outgoing_DB_OP.add(c_o)
            return HttpResponse('添加成功！！！')
    return render(request,"Outgoing/wc_bl.html")


def ss(request):

    return render(request,"FoodManage.html")



def ss_xx(request):

    return render(request,"FoodManage.html")

#护理内容
def hn_homepage(request):
    return render(request, 'ServerContent/NursingContent.html')

def hn(request):
    pk = request.GET.get('pk')
    if(pk!=None):
        sc = get_object_or_404(NursingItemInfo, itemID=pk)
        sc.delete()
    post_list = NursingItemInfo.objects.all()
    if request.method == 'POST':
        SC_id = request.POST['SC_id']
        SC_content = request.POST['SC_content']
        SC_type = request.POST['SC_type']
        q = Q()
        if(SC_id!=""):
            q = q & Q(itemID = SC_id)
        if (SC_content != ""):
            q = q & Q(name = SC_content)
        if (SC_type != ""):
            itemType = NursingTypeInfo.objects.filter(name=SC_type)
            if(itemType.exists()):
                itemType = get_object_or_404(NursingTypeInfo, name=SC_type)
                q = q & Q(itemType = itemType)
        post_list = NursingItemInfo.objects.filter(q)
    length = len(post_list)
    return render(request, 'ServerContent/NursingItem_xx.html', context={'post_list': post_list, 'length':length})

def hn_add(request):
    add_ok = "ok"
    if request.method == 'POST':
        SC_id = request.POST['SC_id']
        SC_content = request.POST['SC_content']
        SC_type = request.POST['SC_type']
        price = request.POST['price']
        is_addValue = request.POST['is_addValue']
        if(is_addValue=="是"):
            is_addValue = True
        else:
            is_addValue = False
        is_Start = request.POST['is_Start']
        if(is_Start=="是"):
            is_Start = True
        else:
            is_Start = False
        Details = request.POST['Details']
        itemType = get_object_or_404(NursingTypeInfo, name=SC_type)
        sc = NursingItemInfo(price=price, itemID=SC_id, name=SC_content, itemType=itemType, addedService=is_addValue, status=is_Start)
        if(Details!=""):
            sc.details = Details
        tag = NursingItemInfo.objects.filter(itemID=SC_id)
        if(tag.exists()):
            add_ok = "false"
        else:
            sc.save()
    return render(request, 'ServerContent/NursingItem_bl_sg.html', context={'add_ok': add_ok})

def sc_detail(request, pk):
    sc = get_object_or_404(NursingItemInfo, pk=pk)
    if request.method == 'POST':
        sc.itemID = request.POST['SC_id']
        sc.name = request.POST['SC_content']
        SC_type = request.POST['SC_type']
        itemType = get_object_or_404(NursingTypeInfo, name=SC_type)
        sc.itemType = itemType
        sc.price = request.POST['price']
        is_addValue = request.POST['is_addValue']
        if (is_addValue == "是"):
            is_addValue = True
        else:
            is_addValue = False
        is_Start = request.POST['is_Start']
        if (is_Start == "是"):
            is_Start = True
        else:
            is_Start = False
        sc.addedService = is_addValue
        sc.status = is_Start
        sc.details = request.POST['Details']
        sc.save()
    return render(request, 'ServerContent/NursingItem Detail.html', context={'post': sc})

#床位管理+护理级别
def homepage(request):
    return render(request, 'srbed/homepage.html')

def sr_homepage(request):
    return render(request, 'srbed/sr_homepage.html')

def houseop(request):
    pk = request.GET.get('pk')
    if(pk!=None):
        room = get_object_or_404(Room, RoomId=pk)
        room.delete()
    post_list = Room.objects.all()
    if request.method == 'POST':
        Id = request.POST['RoomId']
        State = request.POST['RoomState']
        Function = request.POST['RoomFunction']
        BedNum = request.POST['RoomBedNum']
        Rank = request.POST['RoomRank']
        q = Q()
        if(Id!=""):
            q = q & Q(RoomId = Id)
        if (State != ""):
            q = q & Q(RoomState = State)
        if (Function != ""):
            q = q & Q(RoomFunction = Function)
        if (BedNum != ""):
            q = q & Q(RoomBedNum = BedNum)
        if (Rank != ""):
            q = q & Q(RoomRank = Rank)
        post_list = Room.objects.filter(q)
    length = len(post_list)
    return render(request, 'srbed/Houseop.html', context={'post_list': post_list, 'length':length})

def bedop(request):
    pk = request.GET.get('pk')
    if(pk!=None):
        bed= get_object_or_404(Bed, BedId=pk)
        bed.delete()
    post_list = Bed.objects.all()
    if request.method == 'POST':
        BedId = request.POST['BedId']
        BedStart = request.POST['BedStart']
        BedEnd = request.POST['BedEnd']
        CustomerId = request.POST['CustomerId']
        RoomId = request.POST['RoomId']
        q = Q()
        if(BedId!=""):
            q = q & Q(BedId = BedId)
        if (BedStart != ""):
            q = q & Q(BedStart = BedStart)
        if (BedEnd != ""):
            q = q & Q(BedEnd = BedEnd)
        if (CustomerId != ""):
            q = q & Q(CustomerId = CustomerId)
        if (RoomId != ""):
            room = get_object_or_404(Room, RoomId=RoomId)
            q = q & Q(Room=room)
        post_list = Bed.objects.filter(q)
    length = len(post_list)
    return render(request, 'srbed/bedop.html', context={'post_list': post_list, 'length':length})

def sc_detail(request, pk):
    sc = get_object_or_404(NursingItemInfo, pk=pk)
    if request.method == 'POST':
        sc.SC_id = request.POST['SC_id']
        sc.SC_content = request.POST['SC_content']
        sc.SC_type = request.POST['SC_type']
        sc.price = request.POST['price']
        sc.is_addValue = request.POST['is_addValue']
        sc.is_Start = request.POST['is_Start']
        sc.Details = request.POST['Details']
        sc.save()
    return render(request, 'srbed/NursingItem Detail.html', context={'post': sc})

def sr_detail(request, pk):
    sr = get_object_or_404(ServerRank, pk=pk)
    flag = request.GET.get('flag')
    if(flag):
        sr.delete()
        return redirect(reverse('User_manager:SR'))
    else:
        if request.method == 'POST':
            sr.SR_id = request.POST['id']
            sr.SR_rank = request.POST['rank']
            sr.SR_standard = request.POST['standard']
            sr.save()
    return render(request, 'srbed/sr_detail.html', context={'post': sr})

def detail(request,pk):
    room = get_object_or_404(Room, RoomId=pk)
    flag = request.GET.get('flag')
    if(flag):
        room.delete()
        return redirect(reverse('User_manager:houseop'))
    else:
        if request.method == 'POST':
            room.RoomId = request.POST['RoomId']
            room.RoomArea = request.POST['RoomArea']
            room.RoomState = request.POST['RoomState']
            room.RoomFunction = request.POST['RoomFunction']
            room.RoomBedNum = request.POST['RoomBedNum']
            room.RoomRank = request.POST['RoomRank']
            room.save()
        return render(request, 'srbed/House detail.html', context={'post': room})

def bed_detail(request, pk):
    bed = get_object_or_404(Bed, BedId=pk)
    if request.method == 'POST':
        bed.BedId = request.POST['BedId']
        bed.BedState = request.POST['BedState']
        RoomId = request.POST['RoomId']
        room = get_object_or_404(Room, RoomId=RoomId)
        bed.Room = room
        bed.BedStart = request.POST['BedStart']
        bed.BedEnd = request.POST['BedEnd']
        bed.CustomerId = request.POST['CustomerId']
        if(bed.CustomerId!='null'):
            csr = get_object_or_404(Customer, customerID=bed.CustomerId)
        bed.Details = request.POST['Details']
        bed.save()
    return render(request, 'srbed/Bed detail.html', context={'post': bed})

def add(request):
    add_ok = "ok"
    if request.method == 'POST':
        RoomId = request.POST['RoomId']
        RoomArea = request.POST['RoomArea']
        RoomState = request.POST['RoomState']
        RoomFunction = request.POST['RoomFunction']
        RoomBedNum = request.POST['RoomBedNum']
        RoomRank = request.POST['RoomRank']
        room = Room(RoomId=RoomId, RoomArea=RoomArea, RoomState=RoomState, RoomFunction=RoomFunction, RoomBedNum=RoomBedNum, RoomRank= RoomRank)
        tag = Room.objects.filter(RoomId=RoomId)
        if(tag.exists()):
            add_ok = "false"
        else:
            room.save()
    return render(request, 'srbed/House Popup.html', context={'add_ok': add_ok})

def bed_add(request):
    add_ok = "ok"
    if request.method == 'POST':
        BedId = request.POST['BedId']
        BedState = request.POST['BedState']
        roomid = request.POST['houseId']
        BedStart = request.POST['RzTime']
        BedEnd = request.POST['TzTime']
        CustomerId = request.POST['CustomerId']
        Details = request.POST['Details']
        room = get_object_or_404(Room, RoomId=roomid)
        bed = Bed(BedId=BedId, BedState=BedState, Room=room)
        if(BedStart!=""):
            bed.BedStart = BedStart
        if(BedEnd!=""):
            bed.BedEnd = BedEnd
        if(CustomerId!=""):
            bed.CustomerId = CustomerId
            csr = get_object_or_404(Customer, customerID=bed.CustomerId)
        if(Details!=""):
            bed.Details = Details
        tag = Bed.objects.filter(BedId=BedId)
        if(tag.exists()):
            add_ok = "false"
        else:
            bed.save()
    return render(request, 'srbed/Bed Popup.html', context={'add_ok': add_ok})


def sr_add(request):
    add_ok = "ok"
    if request.method == 'POST':
        SR_id = request.POST['SR_id']
        SR_rank = request.POST['SR_rank']
        SR_standard = request.POST['SR_standard']
        sr = ServerRank(SR_id=SR_id, SR_rank=SR_rank, SR_standard=SR_standard)
        tag = ServerRank.objects.filter(SR_id=SR_id)
        if(tag.exists()):
            add_ok = "false"
        else:
            sr.save()
    return render(request, 'srbed/ServerR Popup.html', context={'add_ok': add_ok})


def sr_detail(request, pk):
    sr = get_object_or_404(ServerRank, SR_id=pk)
    if request.method == 'POST':
        sr.SR_id = request.POST['SR_id']
        sr.SR_rank = request.POST['SR_rank']
        sr.SR_standard = request.POST['SR_standard']
        sr.save()
    return render(request, 'srbed/ServerR detail.html', context={'post': sr})

def SC(request):
    add_ok = "ok"
    post_list = NursingItemInfo.objects.all()
    if request.method == 'POST':
        op = request.GET.get('op')
        if(op=='1'):
            SC_id = request.POST['SC_id']
            SC_content = request.POST['SC_content']
            q = Q()
            if (SC_id != ""):
                q = q & Q(SC_id=SC_id)
            if (SC_content != ""):
                q = q & Q(SC_content=SC_content)
            post_list = NursingItemInfo.objects.filter(q)
        elif(op=='2'):
            UserID = request.POST['UserID']
            ItemNumber = request.POST['ItemNumber']
            CitemN = CitemNum(customerID=UserID, ItemNum=ItemNumber)
            csr = get_object_or_404(Customer, customerID=UserID)
            tag = CitemNum.objects.filter(customerID=UserID)
            if (tag.exists()):
                add_ok = "false"
            else:
                CitemN.save()
    length = len(post_list)
    return render(request, 'srbed/ServerC.html', context={'post_list':post_list, 'length':length, 'add_ok': add_ok})

def SR(request):
    pk = request.GET.get('pk')
    if(pk!=None):
        sr= get_object_or_404(ServerRank, SR_id=pk)
        sr.delete()
    post_list = ServerRank.objects.all()
    if request.method == 'POST':
        q = Q()
        SR_id = request.POST['SR_id']
        SR_standard = request.POST['SR_standard']
        if (SR_id != ""):
            q = q & Q(SR_id=SR_id)
        if (SR_standard != ""):
            q = q & Q(SR_standard=SR_standard)
        post_list = ServerRank.objects.filter(q)
    length = len(post_list)
    return render(request, 'srbed/ServerR.html', context={'post_list':post_list, 'length':length})


def ServerInfo(request):
    pk = request.GET.get('pk')
    if(pk!=None):
        cn= get_object_or_404(CitemNum, customerID=pk)
        cn.delete()
    post_list = CitemNum.objects.all()
    bed_list = []
    rank_list = []
    yld_list = []
    for post in post_list:
        CustomerId = post.customerID
        bed = Bed.objects.filter(CustomerId = CustomerId)
        if(bed.exists()):
            bed = get_object_or_404(Bed, CustomerId = CustomerId)
        else:
            bed = None
        sr_list = ServerRank.objects.all()
        for sr in sr_list:
            x,y = sr.SR_standard.split("-", 1)
            if(int(post.ItemNum)>=int(x) and int(post.ItemNum)<=int(y)):
                rank = sr.SR_rank
                yld = sr.SR_standard
                break
        bed_list.append(bed)
        rank_list.append(rank)
        yld_list.append(yld)
    length = len(post_list)
    return render(request, 'srbed/ServerInfo.html', context={'post_list':post_list, 'length':length, 'bed_list':bed_list, 'rank_list':rank_list, 'yld_list':yld_list})

#膳食管理
def kh_change(request, pk):
	if request.POST:
		staffName = request.POST.get('staffName')
		staffId = request.POST.get('staffId')
		customerName = request.POST.get('customerName')
		print(customerName)
		customerId = request.POST.get('customerId')
		remarks = request.POST.get('remarks')
		# 对传来的信息进行包装，包装成customer对象。
		p = ServiceTable(staffName=staffName,
					staffId=staffId,
					customerName=customerName,
					customerId=customerId,
					remarks=remarks)
		p.save()
	ST = get_object_or_404(ServiceTable, customerId=pk)
	return render(request, "ssrl/sz_detail.html", context={'post': ST})


def kh_add(request):
	if request.POST:
		staffName = request.POST.get('staffName')
		staffId = request.POST.get('staffId')
		customerName = request.POST.get('customerName')
		print(customerName)
		customerId = request.POST.get('customerId')
		remarks = request.POST.get('remarks')
		# 对传来的信息进行包装，包装成customer对象。
		p = ServiceTable(staffName=staffName,
					staffId=staffId,
					customerName=customerName,
					customerId=customerId,
					remarks=remarks)
		p.save()
	return render(request, "ssrl/sz_bl_sg.html")



def sdlr(request):
	pk = request.GET.get('pk')
	if (pk != None):
		ST = get_object_or_404(ServiceTable, customerId=pk)
		ST.delete()
	post_list = ServiceTable.objects.all()
	if request.method == 'POST':
		q = Q()
		idk = request.POST['idk']
		idh = request.POST['idh']
		if (idk != ""):
			q = q & Q(customerId=idk)
		if (idh != ""):
			q = q & Q(staffId=idh)
		post_list = ServiceTable.objects.filter(q)
	length = len(post_list)
	return render(request, 'ssrl/sz_xx.html', context={'post_list': post_list, 'length':length})

def ssrl(request):
	pk = request.GET.get('pk')
	if (pk != None):
		ST = get_object_or_404(MealCalendarInfo, id=pk)
		ST.delete()
	post_list = MealCalendarInfo.objects.all()
	if request.method == 'POST':
		q = Q()
		idu = request.POST['id']
		offer_day = request.POST['offerDay']
		offer_time = request.POST['offerTime']
		if (idu != ""):
			q = q & Q(id=idu)
		if (offer_day != ""):
			q = q & Q(offerDay=offer_day)
		if (offer_time != ""):
			q = q & Q(offerTime=offer_time)
		post_list = MealCalendarInfo.objects.filter(q)
	length = len(post_list)
	return render(request, 'ssrl/FoodCalendar_xx.html', context={'post_list': post_list, 'length':length})

def ssrl_add(request):
	if request.POST:
		id = request.POST.get('id')
		mealID_id = request.POST.get('mealID_id')
		offerDay = request.POST.get('offerDay')
		offerTime = request.POST.get('offerTime')
		# 对传来的信息进行包装，包装成customer对象。
		a = MealCalendarInfo(id=id,
					mealID=mealID_id,
					offerDay=offerDay,
					offerTime=offerTime)
		a.save()
	return render(request, "ssrl/FoodCalendar_bl_sg.html")

def ssrl_change(request, pk):
	if request.POST:
		id = request.POST.get('id')
		mealID_id = request.POST.get('mealID_id')
		offerDay = request.POST.get('offerDay')
		offerTime = request.POST.get('offerTime')
		# 对传来的信息进行包装，包装成customer对象。
		p = MealCalendarInfo(id=id,
					mealID=mealID_id,
					offerDay=offerDay,
					offerTime=offerTime)
		p.save()
	ST = get_object_or_404(MealCalendarInfo, id=pk)
	return render(request, "ssrl/FoodCalendar_modify.html", context={'post': ST})

def ssck(request):
	pk = request.GET.get('pk')
	if (pk != None):
		ST = get_object_or_404(MealStorageInfo, mealID=pk)
		ST.delete()
	post_list = MealStorageInfo.objects.all()
	if request.method == 'POST':
		q = Q()
		mealID = request.POST['mealID']
		name = request.POST['name']
		mealType = request.POST['mealType']
		label = request.POST['label']
		if (mealID != ""):
			q = q & Q(mealID=mealID)
		if (name != ""):
			q = q & Q(name=name)
		if (mealType != ""):
			q = q & Q(mealType=mealType)
		if (label != ""):
			q = q & Q(label=label)
		post_list = MealStorageInfo.objects.filter(q)
	length = len(post_list)
	return render(request, 'ssrl/FoodHouse_xx.html', context={'post_list': post_list, 'length':length})

def ssck_add(request):
	if request.POST:
		mealID = request.POST.get('mealID')
		name = request.POST.get('lname')
		mealType = request.POST.get('mealType')
		price = request.POST.get('price')
		label = request.POST.get('label')
		muslim = request.POST.get('muslim')
		offerWeek = request.POST.get('offerWeek')
		status = request.POST.get('status')


		# 对传来的信息进行包装，包装成customer对象。
		p = MealStorageInfo(mealID = mealID,
						 name = name,
						 mealType = mealType,
						 price=price,
						 label=label,
						 muslim=muslim,
						 offerWeek=offerWeek,
						 status=status)
		p.save()
	return render(request, "ssrl/FoodHouse_bl_sg.html")

def ssck_change(request, pk):
	if request.POST:
		mealID = request.POST.get('mealID')
		name = request.POST.get('name')
		mealType = request.POST.get('mealType')
		price = request.POST.get('price')
		label = request.POST.get('label')
		muslim = request.POST.get('muslim')
		offerWeek = request.POST.get('offerWeek')
		status = request.POST.get('status')
		# 对传来的信息进行包装，包装成customer对象。
		p = MealStorageInfo(mealID = mealID,
						 name = name,
						 mealType = mealType,
						 price=price,
						 label=label,
						 muslim=muslim,
						 offerWeek=offerWeek,
						 status=status)
		p.save()
	ST = get_object_or_404(MealStorageInfo, mealID=pk)
	return render(request, "ssrl/FoodStorage_modify.html", context={'post': ST})

# 返回用户管理的初始界面
def customer_manage_test(request):
    return render(request, "ssrl/szfldx.html")

def FoodCalendar(request):
    return render(request, "ssrl/FoodCalendar.html")

def FoodHouse(request):
    return render(request, "ssrl/FoodHouse_xx.html")

def FoodCalendar_xx(request):
    return render(request, "ssrl/FoodCalendar_xx.html")

