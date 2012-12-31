from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from moonline.models import *


@twilio_view
def answer(request):
    r = Response()
    r.say('Thanks for calling the moon line.')
    return r
    

@twilio_view
def read(request):
    r = Response()
    r.sms('Thanks for the SMS message!')
    return r