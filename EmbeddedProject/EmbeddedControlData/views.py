from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import WorkingData
import datetime

from django.core import serializers


# Create your views here.
def getData(request):
    now = datetime.datetime.now()
    if request.method == 'GET':
        try:
            obj = WorkingData.objects.all().first()
            response = {
                'exist': True,
                'current_hour': now.hour,
                'current_minute': now.minute,
                'turn_off_led_if_light': obj.turn_off_led_if_light,
                'light_start_hour': obj.light_start_hour,
                'light_end_hour': obj.light_end_hour,
                'ambient_temp': obj.ambient_temp,
                'ambient_humidity': obj.ambient_humidity,
                'soil_humidity': obj.soil_humidity,
                'check_period': obj.check_period
            }
            return JsonResponse(response)
        except:
            return JsonResponse({'exist': False})

    return HttpResponse("hello")


def getCurrentHour(request):
    now = datetime.datetime.now()
    if request.method == 'GET':
        try:
            return HttpResponse(now.hour)
        except:
            return HttpResponse(-1)

    return HttpResponse("hello")


def getCurrentMinute(request):
    now = datetime.datetime.now()
    if request.method == 'GET':
        try:
            return HttpResponse(now.minute)
        except:
            return HttpResponse(-1)

    return HttpResponse("hello")


def getTurnOffLEDIfLight(request):
    if request.method == 'GET':
        try:
            obj = WorkingData.objects.all().first()
            return HttpResponse(obj.turn_off_led_if_light)
        except:
            return HttpResponse(-1)

    return HttpResponse("hello")


def getLightStartHour(request):
    if request.method == 'GET':
        try:
            obj = WorkingData.objects.all().first()
            return HttpResponse(obj.light_start_hour)
        except:
            return HttpResponse(-1)

    return HttpResponse("hello")


def getLightEndHour(request):
    if request.method == 'GET':
        try:
            obj = WorkingData.objects.all().first()
            return HttpResponse(obj.light_end_hour)
        except:
            return HttpResponse(-1)

    return HttpResponse("hello")


def getAmbientTemp(request):
    if request.method == 'GET':
        try:
            obj = WorkingData.objects.all().first()
            return HttpResponse(obj.ambient_temp)
        except:
            return HttpResponse(-1)

    return HttpResponse("hello")


def getAmbientHumidity(request):
    if request.method == 'GET':
        try:
            obj = WorkingData.objects.all().first()
            return HttpResponse(obj.ambient_humidity)
        except:
            return HttpResponse(-1)

    return HttpResponse("hello")


def getSoilHumidity(request):
    if request.method == 'GET':
        try:
            obj = WorkingData.objects.all().first()
            return HttpResponse(obj.soil_humidity)
        except:
            return HttpResponse(-1)

    return HttpResponse("hello")


def getCheckPeriod(request):
    if request.method == 'GET':
        try:
            obj = WorkingData.objects.all().first()
            return HttpResponse(obj.check_period)
        except:
            return HttpResponse(-1)

    return HttpResponse("hello")


def setData(request):

    turn_off_led_if_light = int(request.GET.get('turn_off_led_if_light', 1))
    light_start_hour = int(request.GET.get('light_start_hour', 6))
    light_end_hour = int(request.GET.get('light_end_hour', 19))
    ambient_temp = int(request.GET.get('ambient_temp', 30))
    ambient_humidity = int(request.GET.get('ambient_humidity', 50))
    soil_humidity = int(request.GET.get('soil_humidity', 50))
    check_period = int(request.GET.get('check_period', 10))

    try:
        obj = WorkingData.objects.all().first()
        obj.delete()
    except:
        pass

    w = WorkingData(turn_off_led_if_light=turn_off_led_if_light,
                    light_start_hour=light_start_hour,
                    light_end_hour=light_end_hour,
                    ambient_temp=ambient_temp,
                    ambient_humidity=ambient_humidity,
                    soil_humidity=soil_humidity,
                    check_period=check_period)
    w.save()
    return HttpResponse("success")
