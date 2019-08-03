# -*- coding: utf-8 -*-


class Service(object):
    clientID = ''
    itemID = ''
    time = ''

    def __init__(self, client_id, item_id, time):
        # 在构造函数里解决默认值的问题
        self.clientID = client_id
        self.itemID = item_id
        self.time = time

