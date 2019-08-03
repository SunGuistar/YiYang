# -*- coding: utf-8 -*-


class NursingItem(object):
    # 护理项目类描述
    # 护理项目ID不必填写，不能修改，由系统自动生成
    name = ''
    price = 0               # 护理价格的单位是（元/周）
    addedService = True     # 是否有增值服务（不明白是做什么的）
    details = ''            # 护理内容的描述
    status = True           # 这个属性表示该项护理内容是否启用（可以被购买）
    itemType = ''           # 这个属性是护理类型的名称（*是名称不是ID）

    def __init__(self, name, price, item_type, added_service=False, details='', status=True):
        # 各项属性的初始化
        self.name = name
        self.price = price
        self.addedService = added_service
        self.details = details
        self.status = status
        self.itemType = item_type
