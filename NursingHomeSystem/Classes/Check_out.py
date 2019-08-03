import datetime
import random
from ManageModels.models import *

class Check_out_info(object):

    customerID = ''
    check_out_type = ''
    check_out_reason = ''
    check_out_time = ''
    remark = ''
    time = ''
    check_out_state = False

    def __init__(self,customerID, check_out_type, check_out_reason,check_out_time,time,remark):
        self.customerID = customerID
        self.check_out_type = check_out_type
        self.check_out_reason = check_out_reason
        self.check_out_time = check_out_time
        self.remark = remark

        # 自动生成办理时间
        self.time = time
        self.check_out_state = False
