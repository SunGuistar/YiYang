"""NursingHomeSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Interface import view
from Interface import NursingItemInterface, NursingTypeInterface, Test, StaffInterface, ServiceAttentionInterface
from Interface import MainInterface
from django.conf.urls import url
from Interface import  check_out_views, customer_views

urlpatterns = [
# 测试用
    path('init/', Test.init_staff_position_type),
    path('test/', Test.test),
    path('test2/', Test.test2),

# 合用户管理
    path('user/main', Test.my_main),
    path('user/welcome.html', MainInterface.welcome),
    path('user/yhgl.html', MainInterface.yghl),
    path('user/search.html', MainInterface.search),
    path('user/yh_lr1.html', MainInterface.yh_lr1),

    # 用户表格页面
    path('user/yh_lr2.html', MainInterface.yh_lr2),
    path('user/yh_lr2_data.html', MainInterface.yh_lr2_data),
    path('user/yh_lr2_delete.html', MainInterface.yh_lr2_remove),

    path('user/yh_table.html', MainInterface.yh_table),
    path('user/yh_table_data.html', MainInterface.yh_table_data),
    # 查看客户详细信息
    path('user/yh_info_table.html', MainInterface.yh_info_table),
    # 修改客户详细信息
    path('user/yh_edit_table.html', MainInterface.yh_edit_table),
    path('user/yh_edit_table_data.html', MainInterface.yh_edit_table_data),
    path('user/yh_edit_table_modify.html', MainInterface.yh_edit_table_modify),
    # 这个是废网页
    path('user/yh_xx.html', MainInterface.yh_xx),


# 合服务关注
    path('user/fwgz/khxxcx.html', MainInterface.khxxcx),
    path('user/fwgz/khxxcx_data.html', MainInterface.khxxcx_data),

    path('user/fwgz/khfwgz.html', MainInterface.khfwgz),
    path('user/fwgz/khfwgz_data.html', MainInterface.khfwgz_data),
    path('user/fwgz/khfwgz_renew.html', MainInterface.khfwgz_renew),
    path('user/fwgz/khfwgz_delete.html', MainInterface.khfwgz_delete),

    path('user/fwgz/dxffgm.html', MainInterface.dxffgm),
    path('user/fwgz/dxffgm_data.html', MainInterface.dxffgm_data),
    path('user/fwgz/dxffgm_buy.html', MainInterface.dxffgm_buy),

    path('user/fwgz/jyjl.html', MainInterface.jyjl),
    path('user/fwgz/jyjl_data.html', MainInterface.jyjl_data),

    path('user/fwgz/xxxx.html', MainInterface.xxxx),
    path('user/fwgz/xxxx2.html', MainInterface.xxxx2),
    path('user/fwgz/xxxx_data.html', MainInterface.xxxx_data),
    # ---------------------------------------------------------------------- #

# 东源兄 外出登记

    # 导航页
    url(r'^user/wc.html$', view.wc),
    # 新增页
    url(r'^user/wc_bl.html$', view.wc_add1),
    url(r'^user/wcbl$', view.wc_add1),
    # 信息页
    url(r'^user/wc_xx.html$', view.wc_xx_html),
    url(r'^user/wcxx$', view.wc_xx),
    # 删除页
    url(r'^user/wcremove1$', view.wc_remove1),
    url(r'^user/wcremove2$', view.wc_remove2),
    # 其他
    url(r'^user/wcbacktime1$', view.wc_hydj1),
    url(r'^user/wcbacktime2$', view.wc_hydj2),
    # 审核 修改
    url(r'^user/wcverify1$', view.wc_verify1),
    url(r'^user/wcmodify$', view.modify1),

# 姜莱兄：退住登记模块 晓春

    url(r'^user/tz.html$', check_out_views.tz),
    url(r'^user/tz_xx.html$', check_out_views.tz1),
    url(r'^user/tzxx$', check_out_views.tz_xx),
    url(r'^user/remove1$', check_out_views.tz_remove1),
    url(r'^user/verify1$', check_out_views.tz_verify1),
    url(r'^user/remove2$', check_out_views.tz_remove2),
    url(r'^user/verify2$', check_out_views.tz_verify2),
    url(r'^user/modify$', check_out_views.tz_modify),

    url(r'^user/tz_bl_sg.html$', check_out_views.tz_add1),
    url(r'^user/tzbl$', check_out_views.tz_add1),

# 马骁：入住登记

    url(r'^user/init_service.html$', MainInterface.init_service),
    # 导航页    搞定
    url(r'^user/customer.html$', customer_views.customer_manage),

    # 信息页面   搞定
    url(r'^user/CheckIn_xx.html$', customer_views.customer_info_html),
    url(r'^user/CheckIn_xx$', customer_views.customer_info),

    # 新增页面   1/2搞定
    url(r'^user/CheckIn_info_add.html$', customer_views.CheckIn_info_add_html),
    url(r'^user/CheckIn_info_add$', customer_views.CheckIn_info_add),

    url(r'^user/CheckIn_info_add1.html$', customer_views.CheckIn_info_add1_html),
    url(r'^user/CheckIn_info_add1$', customer_views.CheckIn_info_add1),
    # 删除 1/2
    url(r'^user/cin_remove1$', customer_views.Check_in_remove1),
    url(r'^user/cin_remove2$', customer_views.Check_in_remove2),
    # 修改 搞定
    url(r'^user/cin_modify$', customer_views.Check_in_modify),
    # 详细信息 搞定2/5
    # 页头信息  搞定
    url(r'^user/customer_show.html$', customer_views.customer_show_html),
    url(r'^user/customer_show', customer_views.customer_show),
    # 基本信息  搞定
    url(r'^user/CheckIn_bl_sg.html$', customer_views.CheckIn_bl_sg_html),
    url(r'^user/CheckIn_bl_sg$', customer_views.CheckIn_bl_sg),
    # 床位信息  正在搞 1/2 等待合并
    url(r'^user/BedsInfo.html$', customer_views.BedInfo_html),
    url(r'^user/BedsInfo$', customer_views.BedInfo),
    # 护工信息   正在搞
    url(r'^user/NersingWorker Info.html$', customer_views.NersingWorker_Info_html),
    url(r'^user/NersingWorker_Info$', customer_views.NersingWorker_Info),
    # 套餐信息   未搞...
    url(r'^user/SetMeal.html$', customer_views.SetMeal_html),
    url(r'^user/SetMeal$', customer_views.SetMeal),

# 晓春兄：登录测试
    url(r'^login$', customer_views.login),
    url(r'^user/login$', customer_views.login),
    url(r'^user/logout$', customer_views.logout),
    url(r'^Verification$', customer_views.verify),

# ---------------------------------------------------------------------- #
# 正式的员工信息path
    path('add_staff_info/', StaffInterface.add_staff),

# 比较正式的护理类型path
    path('add_nursing_type/', NursingTypeInterface.add_nursing_type),
    path('search_nursing_type/', NursingTypeInterface.search_nursing_type),
    path('remove_nursing_type/', NursingTypeInterface.remove_nursing_type),
    path('modify_nursing_type/', NursingTypeInterface.modify_nursing_type),

# 比较正式的护理项目path
    path('add_nursing_item/', NursingItemInterface.add_nursing_item),

# 正式的服务关注path
    path('init_service_list/', ServiceAttentionInterface.init_service_list),
    path('add_service/', ServiceAttentionInterface.add_service),
    path('renew_service/', ServiceAttentionInterface.renew_service),
    path('show_service/', ServiceAttentionInterface.show),


#护理内容
    url(r'^user/ServerContent/$', view.hn_homepage),
    url(r'^user/hn_manager/hn/$', view.hn, name='hn'),
    url(r'^user/hn_manager/hn/add/$', view.hn_add, name='hn_add'),
    url(r'^user/hn_manager/hn/nurseI/([0-9]+)/$', view.sc_detail, name='sc_detail'),

#床位管理
    url(r'^user/br_manager/$', view.homepage, name='homepage'),
    url(r'^user/br_manager/room_manage/$', view.houseop, name='houseop'),
    url(r'^user/br_manager/room_manage/room_add/$', view.add, name='add'),
    url(r'^user/br_manager/room_manage/room/([0-9]+)/$', view.detail, name='detail'),
    url(r'^user/br_manager/bed_manage/$', view.bedop, name='bedop'),
    url(r'^user/br_manager/bed_manage/bed_add/$', view.bed_add, name='bed_add'),
    url(r'^user/br_manager/bed_manage/bed/([0-9]+)/$', view.bed_detail, name='bed_detail'),

#护理级别
    url(r'^user/sr_manager/$', view.sr_homepage, name='sr_homepage'),
    url(r'^user/sr_manager/ServerR/$', view.SR, name='SR'),
    url(r'^user/sr_manager/ServerC/$', view.SC, name='SC'),
    url(r'^user/sr_manager/ServerR/serverR_add/$', view.sr_add, name='sr_add'),
    url(r'^user/sr_manager/ServerR/sr/([0-9]+)/$', view.sr_detail, name='sr_detail'),
    url(r'^user/sr_manager/ServerInfo/$', view.ServerInfo, name='ServerInfo'),


#ssrl
    url(r'^user/FoodCalendar/$', view.FoodCalendar),

    path('user/FoodCalendar/FoodHouse_xx/', view.ssck),
    path('user/FoodCalendar/FoodHouse_xx/add', view.ssck_add),
    url(r'^user/FoodCalendar/FoodHouse_xx/change1/([0-9]+)/$', view.ssck_change, name='ssck_change'),

    path('user/FoodCalendar/FoodCalendar_xx', view.ssrl),
    path('user/FoodCalendar/FoodCalendar_xx/add', view.ssrl_add),
    url(r'^user/FoodCalendar/change/([0-9]+)/$', view.ssrl_change, name='ssrl_change'),

    url(r'^user/service/$', view.customer_manage_test),
    path('user/service/sdlr/', view.sdlr),
    path('user/service/sdlr/add/', view.kh_add),
    url(r'^user/service/sdlr/change/([0-9]+)/$', view.kh_change, name='kh_change'),

]


