# -*- coding: utf-8 -*-

from ManageModels.models import *
from django.db.models import Q


class UserOperate(object):
    @staticmethod
    def search(username='', position='', status=''):
        q = Q()
        if username != '':
            q = q & Q(username=username)
        if position != '':
            q = q & Q(position=position)
        if status != '':
            q = q & Q(status=status)

        s_list = UserInfo.objects.filter(q)
        return s_list

    @staticmethod
    def modify_password(users, password):
        for user in users:
            user.password = password
            user.save()

    @staticmethod
    def modify_status(users, status):
        for user in users:
            user.status = status
            user.save()

    @staticmethod
    def login(username, password, position):
        u = UserInfo.objects.filter(username=username, password=password, position=position)
        if len(u) == 1:
            return True
        else:
            return False

