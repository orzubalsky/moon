from django.conf import settings
from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from pywunderground import request as weather
from moonline.models import *


@twilio_view
def answer(request):
    r = Response()
    r.say('Thanks for calling the moon line.')
    
    print request
    return r
    

@twilio_view
def read(request):
    r = Response()
    r.sms('Thanks for the SMS message!')
    return r
    
    
def moon_over_location(location="New York, NY"):
    return weather(settings.WEATHER_KEY_ID, ['astronomy',], location)