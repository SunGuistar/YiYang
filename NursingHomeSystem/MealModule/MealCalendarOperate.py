# -*- coding: utf-8 -*-

from ManageModels.models import MealCalendarInfo, MealStorageInfo


class MealCalendarOperate(object):
    @staticmethod
    def add_calendar(meal_id, offer_day, offer_time):
        meal = MealStorageInfo.objects.get(mealID=meal_id)
        MealCalendarInfo(meal, offer_day, offer_time).save()

    @staticmethod
    def show_day(offer_day):
        return MealCalendarInfo.objects.filter(offerDay=offer_day)

    @staticmethod
    def show_all():
        return MealCalendarInfo.objects.all()

    @staticmethod
    def search(cal_id):
        return MealCalendarInfo.objects.get(id=cal_id)

    @staticmethod
    def remove(cal_id):
        cal = MealCalendarOperate.search(cal_id)
        cal.delete()

    @staticmethod
    def modify(meal_id, offer_day, offer_time):
        meal = MealCalendarInfo.objects.get(mealID=meal_id)
        meal.offerDay = offer_day
        meal.offerTime = offer_time
        meal.save()
