from django.urls import path

from . import views

urlpatterns = [
    path('', views.getData),
    path('ChangeData', views.setData),
    path('current_hour', views.getCurrentHour),
    path('current_minute', views.getCurrentMinute),
    path('turn_off_led_if_light', views.getTurnOffLEDIfLight),
    path('light_start_hour', views.getLightStartHour),
    path('light_end_hour', views.getLightEndHour),
    path('ambient_temp', views.getAmbientTemp),
    path('ambient_humidity', views.getAmbientHumidity),
    path('soil_humidity', views.getSoilHumidity),
    path('check_period', views.getCheckPeriod)
]