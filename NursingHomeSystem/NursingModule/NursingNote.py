# -*- coding: utf-8 -*-

import datetime


class NursingNote(object):
    operatorID = ''
    clientID = ''
    itemID = ''
    time = ''
    remarks = ''

    def __init__(self, operator_id, client_id, item_id, time='', remarks=''):
        self.operatorID = operator_id
        self.clientID = client_id
        self.itemID = item_id
        if time == '':
            self.time = datetime.datetime.now()
        else:
            self.time = time
        self.remarks = remarks
