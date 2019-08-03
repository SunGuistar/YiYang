from django.db import models

# Create your models here.

# Create your models here.

class ServiceTable(models.Model):
    # 主键
    customerId = models.CharField(primary_key=True, max_length=12)

    customerName = models.CharField(max_length=12)
    staffName = models.CharField(max_length=12)
    staffId = models.CharField(max_length=12)
    remarks = models.CharField(max_length=200)

class MealCalendarInfo(models.Model):
    # 记录每一周的膳食日历
    id = models.CharField(primary_key=True, max_length=5)
    mealID = models.CharField(max_length=6)
    offerDay = models.CharField(max_length=6)                   # 星期一、星期二......
    offerTime = models.CharField(max_length=6)                  # 早餐、午餐、晚餐

class MealStorageInfo(models.Model):
    mealID = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=20, unique=True)
    mealType = models.CharField(max_length=10)
    label = models.CharField(max_length=20)                     # 膳食标签
    price = models.CharField(max_length=20)
    offerWeek = models.CharField(max_length=20)
    # offerType = models.CharField(max_length=20)
    muslim = models.BooleanField()                              # 是否清真
    status = models.BooleanField()

#床位管理和护理级别
class Room(models.Model):
    RoomId = models.CharField(max_length=30)
    RoomArea = models.IntegerField()
    RoomState = models.CharField(max_length=20)
    RoomFunction= models.CharField(max_length=20)
    RoomBedNum = models.IntegerField()
    RoomRank = models.IntegerField()

    def _str_(self):
        return self.RoomId

    def get_absolute_url(self):
        return reverse('User_manager:detail', kwargs={'pk':self.pk})

class Bed(models.Model):
    BedId = models.CharField(max_length=30)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    BedState = models.CharField(max_length=20)
    BedStart = models.CharField(max_length=20, default='null')
    BedEnd = models.CharField(max_length=20, default='null')
    CustomerId = models.CharField(max_length=30, default='null')
    Details = models.CharField(max_length=60, default='null')

    def get_absolute_url(self):
        return reverse('User_manager:bed_detail', kwargs={'pk':self.pk})

class ServerRank(models.Model):
    SR_id = models.CharField(max_length=30)
    SR_rank = models.CharField(max_length=30)
    SR_standard = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('User_manager:sr_detail', kwargs={'pk':self.pk})

class CitemNum(models.Model):
    customerID = models.CharField(max_length=12)
    ItemNum = models.CharField(max_length=30)

# 护理管理模块
# 护理类型
class NursingTypeInfo(models.Model):
    typeID = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=20, unique=True)
    details = models.CharField(max_length=100)


# 护理项目
class NursingItemInfo(models.Model):
    itemID = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=40, unique=True)
    price = models.IntegerField()
    addedService = models.BooleanField()
    details = models.CharField(max_length=100)
    status = models.BooleanField()
    itemType = models.ForeignKey('NursingTypeInfo', to_field='typeID', default=1, on_delete=models.CASCADE)


class ServiceInfo(models.Model):
    clientID = models.ForeignKey('Customer', to_field='customerID', default=1, on_delete=models.CASCADE)
    itemID = models.ForeignKey('NursingItemInfo', to_field='itemID', default=1, on_delete=models.CASCADE)
    # 某用户某条服务剩余时间
    remaining = models.IntegerField()
    # 莫用户某条服务的状态（正常、欠费、即将用完）
    status = models.CharField(max_length=8)


class RecordInfo(models.Model):
    # 记录交易时间
    recordTime = models.DateTimeField()
    # 记录交易类型（新增服务、删除服务、续费服务）
    recordType = models.CharField(max_length=12)
    # 交易数量（如：删除xxx服务12周）
    quantity = models.IntegerField()
    # 交易金额 可能还需要限定一下小数位数
    amount = models.IntegerField()
    # 交易者
    clientID = models.ForeignKey('Customer', to_field='customerID', default=1, on_delete=models.CASCADE)
    # 操作员
    operatorID = models.ForeignKey('UserInfo', to_field='username', default=1, on_delete=models.CASCADE)
    # 交易的服务
    itemID = models.ForeignKey('NursingItemInfo', to_field='itemID', default=1, on_delete=models.CASCADE)


# 膳食管理模块
class MealManageInfo(models.Model):
    # 为客户制定膳食
    mealID = models.ForeignKey('MealStorageInfo', to_field='mealID', default=1, on_delete=models.CASCADE)
    clientID = models.ForeignKey('Customer', to_field='customerID', default=1, on_delete=models.CASCADE)
    offerDay = models.CharField(max_length=6)
    offerTime = models.CharField(max_length=6)
    remarks = models.CharField(max_length=50)


# 用户管理模块
class UserInfo(models.Model):
    # 主键
    username = models.CharField(primary_key=True, max_length=12)

    password = models.CharField(max_length=12)
    # 用户类型为医生、护士、护工、管理员等
    position = models.CharField(max_length=10)
    # 用户是否可用
    status = models.CharField(max_length=6)


class StaffInfo(models.Model):
    # 主键
    staffID = models.CharField(primary_key=True, max_length=12)

    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    birthday = models.DateField()
    # 外键，可能需要调整
    staffType = models.ForeignKey('StaffTypeInfo', to_field='staffType', default=1, on_delete=models.CASCADE)
    employeeDate = models.DateField()
    # 外键，可能需要调整
    position = models.ForeignKey('PositionInfo', to_field='position', default=1, on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    introduction = models.CharField(max_length=200)
    remarks = models.CharField(max_length=40)
    # 外键，可能还需调整
    user = models.ForeignKey('UserInfo', to_field='username', default=1, on_delete=models.CASCADE)


class PositionInfo(models.Model):
    # 员工职位表，默认有4条医生、护士、护工、管理员
    positionID = models.CharField(primary_key=True, max_length=2)
    position = models.CharField(max_length=16, unique=True)


class StaffTypeInfo(models.Model):
    # 员工类型表，默认有临时工，合同工，固定工，代训工，实习生等
    typeID = models.CharField(primary_key=True, max_length=2)
    staffType = models.CharField(max_length=16, unique=True)


class NursingNoteInfo(models.Model):
    # 护理记录有，护工ID，客户ID，护理项目ID，备注remarks（可不填），护理时间
    operatorID = models.ForeignKey('StaffInfo', to_field='staffID', default=1, on_delete=models.CASCADE)
    clientID = models.ForeignKey('Customer', to_field='customerID', default=1, on_delete=models.CASCADE)
    itemID = models.ForeignKey('NursingItemInfo', to_field='itemID', default=1, on_delete=models.CASCADE)
    time = models.DateTimeField()
    remarks = models.CharField(max_length=50)

# 退住登记
class Check_out(models.Model):

    # 主键
    customerID = models.CharField(primary_key=True, max_length=12)
    # 退住类型，原因，时间，状态（是否审核），时间，备注。
    check_out_type = models.CharField(max_length=20)
    check_out_reason = models.TextField()
    check_out_time = models.DateField()
    check_out_state = models.BooleanField()
    time = models.DateField()
    remark = models.TextField()


class Customer(models.Model):
    #　主键  一共有25个属性
    customerID = models.CharField(primary_key=True, max_length=12)

    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    nation = models.CharField(max_length=20)
    btype = models.CharField(max_length=4)

    ID_number = models.CharField(max_length=20)
    birthday = models.DateField()

    province =  models.CharField(max_length=20)
    city =  models.CharField(max_length=20)
    area =  models.CharField(max_length=20)
    address =  models.CharField(max_length=40)

    marrige =  models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    height =  models.FloatField()
    weight =  models.FloatField()

    phonenum1 = models.CharField(max_length=11)
    phonenum2 = models.CharField(max_length=11, blank=True, null=True)

    remark =  models.TextField(blank=True,null=True)

    check_in_date = models.DateField()
    check_out_date = models.DateField(blank=True,null=True)
    state_1 =  models.BooleanField()
    state_2 =  models.BooleanField()
    nursing = models.CharField(max_length=10, blank=True, null=True)
    bedID = models.ForeignKey("Bed", to_field='id', default=None, on_delete=models.CASCADE, blank=True, null=True)


#外出管理
class AppInfo(models.Model):
    # 主键
    AppID = models.CharField(primary_key=True,max_length=20,default=1)#申请Id
    name = models.CharField(max_length=20)#姓名
    Cp_name=models.CharField(max_length=20)#陪同人姓名
    Cp_tel = models.CharField(max_length=20)#陪同人电话
    Cp_rela= models.CharField(max_length=20)#陪同人关系
    Ap_stat= models.CharField(blank=1,max_length=20) #状态（是否回院）
    Ap_stat1 = models.CharField(blank=1, max_length=20) #状态（是否审批）
    Remarks=models.TextField()#备注
    Time_ar=models.CharField(blank=1,max_length=20,default=None)#实际回院时间
    Time_er=models.CharField(max_length=20)#预计回院时间
    Time_eo=models.CharField(max_length=20)#预计外出时间
    wcsy=models.TextField()#外出事由


