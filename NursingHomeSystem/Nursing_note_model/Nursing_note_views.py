from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



#导航
def Nursing_note_html(request):
    return render(request, "Nursing_note/hljl.html")
#信息
def Nursing_note_info_html(request):
    return render(request, "Nursing_note/hl_xx.html")


# 这里需要查询数据库中所有信息返回去
# 调用DB_operation中Nursing——note——DB——OP中的函数可以查询
# 返回jsondata对象,类似于这样的，json.dumps()
# var datanow=[
# # 	{"idk":"1","hljb":"1xxxx","idh":"3xx","hltime":"4xx","hlnr":"6xx"},
# # 	{"idk":"8","hljb":"2xxx","idh":"3xxx","hltime":"4xxx","hlnr":"6xxx"},
# # 	{"idk":"7","hljb":"3xxx","idh":"3xxx","hltime":"4xxx","hlnr":"6xxx"},
# # 	{"idk":"6","hljb":"4xxx","idh":"3xxx","hltime":"4xxx","hlnr":"6xxx"},
# # 	{"idk":"5","hljb":"2xxxxx","idh":"3xxx","hltime":"4xxx","hlnr":"6xxx"},
# # 	{"idk":"4","hljb":"5xxx","idh":"3xxx","hltime":"4xxx","hlnr":"6xxx"},
# # 	{"idk":"3","hljb":"5xxx","idh":"3xxx","hltime":"4xxx","hlnr":"6xxx"},
# # ];
def Nursing_note_info(request):
    print(request.POST)
    return HttpResponse("yes")

#增加
def Nursing_note_info_add_html(request):
    return render(request, "Nursing_note/hl_bl_sg.html")

# 这里需要将收到的信息添加到数据库，
# 收到的信息使用request.POST['id']可以提取出来,
# 调用DB_operation中Nursing——note——DB——OP中的函数可以增加
# 返回Httpresponse（内容随便）
def Nursing_note_info_add(request):
    if request.POST:
        operator_id = request.POST.get('operator_id')
        client_id = request.POST.get('client_id')
        item_id = request.POST.get('item_id')
        time = request.POST.get('time')
        remarks = request.POST.get('remarks')
        # 对传来的信息进行包装，包装成customer对象。
        a = MealCalendarInfo(operator_id=operator_id,
                             client_id=client_id,
                             item_id=item_id,
                             time=time,
                             remarks=remarks)
        Nursing_note_DB_OP.add(a)
        a.save()
    print(request.POST)

    return HttpResponse("nihao a")


#删除
# 这里需要将收到的信息数据库删除
# 这里会收到指定的客户ID，根据客户id删除
# 调用DB_operation中Nursing——note——DB——OP中的函数可以
# 返回Httpresponse（内容随便）
def Nursing_note_info_remove(request):
    if request.POST:
        if request.POST.get('client_id'):
            Nursing_note_DB_OP.remove(request.POST.get('client_id'))
    print(request.POST)
    return HttpResponse("nihao a")

# 批量删除，多次调用单个删除即可
def Nursing_note_info_remove1(request):
    print(request.POST)

    return HttpResponse("nihao a")

# 修改
# 这里需要将收到的信息修改
# 收到的信息使用request.POST['xxx']可以提取出来,
# 调用DB_operation中Nursing——note——DB——OP中的函数可以增加
# 返回Httpresponse（内容随便）
def Nursing_note_info_modify(request):
    print('hello')
    nursing_note_modify_dict = dict()
    if request.POST:
        nursing_note_modify_dict.update(request.POST)
        # 打印一下
        for i in request.POST.keys():
            print(i, request.POST[i])
            nursing_note_modify_dict[i] = request.POST[i]
        # 去掉字典中的特殊key-value
        del nursing_note_modify_dict['csrfmiddlewaretoken']
        for i in nursing_note_modify_dict.keys():
            print(i, request.POST[i])

        Nursing_note_DB_OP.modify(nursing_note_modify_dict)

    print(request.POST)
    return HttpResponse("nihao a")

