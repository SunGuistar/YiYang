# -*- coding: utf-8 -*-

from ManageModels.models import NursingNoteInfo, Customer, NursingItemInfo, StaffInfo
from django.db.models import Q


class NursingNoteOperate(object):
    @staticmethod
    def add_note(note):
        operator = StaffInfo.objects.get(staffID=note.operatorID)
        client = Customer.objects.get(customerID=note.clientID)
        item = NursingItemInfo.objects.get(item=note.itemID)
        time = note.time
        remarks = note.remarks

        NursingNoteInfo(operatorID=operator,
                        clientID=client,
                        itemID=item,
                        time=time,
                        remarks=remarks).save()

    @staticmethod
    def search(operator_id='',
               client_id='',
               min_time='',
               max_time=''):
        q = Q()
        if operator_id != '':
            q = q & Q(operatorID=operator_id)
        if client_id != '':
            q = q & Q(clientID=client_id)
        if min_time != '':
            q = q & Q(time__gte=min_time)
        if max_time != '':
            q = q & Q(time__lte=max_time)

        return NursingNoteInfo.objects.filter(q)

    @staticmethod
    def delete(notes):
        for note in notes:
            note.delete()

    @staticmethod
    def modify(note,
               operator_id='',
               client_id='',
               item_id='',
               time='',
               remarks=''):
        if operator_id != '':
            note.operatorID = operator_id
        if client_id != '':
            note.clientID = client_id
        if item_id != '':
            note.itemID = item_id
        if time != '':
            note.time = time
        if remarks != '':
            note.remarks = remarks

