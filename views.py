import os
import urllib
import string
from random import choice
from django.shortcuts import render
from django.http import HttpResponse
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from django.views.decorators.csrf import csrf_exempt
from viberbot.api.messages import TextMessage
from django.conf import settings
from viberbot.api.messages import TextMessage, PictureMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

bot_configuration = BotConfiguration(
	name='UnicornService',
	avatar='',
	auth_token='4a863da4a227d272-425a6b66b594bba-a077ad6679ad30a'
)
viber = Api(bot_configuration)

@csrf_exempt
def set_webhook(request):
	event_types = ["failed","subscribed","unsubscribed","conversation_started"]
	url = f'https://{settings.ALLOWED_HOSTS[1]}/vbot/callback/'
	viber.set_webhook(url = url, webhook_events = event_types)
	return HttpResponse(status=200)

@csrf_exempt
def unset_webhook(request):
    viber.unset_webhook()
    return HttpResponse('webhook drop')

def generate_image_name(m):
    chars = string.ascii_letters + string.digits
    return (''.join([choice(chars) for i in range(m)])+'.jpg')

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)
# viber.send_messages(viber_request.sender.id, TextMessage(text='Hi'))
        if isinstance(viber_request,ViberMessageRequest):
            if isinstance(viber_request.message, TextMessage):
                print(viber_request.message)
                k=viber_request.message
                print(type(k))
                viber.send_messages(viber_request.sender.id,[TextMessage(text='Это текст')])
            elif isinstance(viber_request.message, PictureMessage):
                print(viber_request.message)
                urllib.request.urlretrieve(viber_request.message.media, "media/"+generate_image_name(10))
                viber.send_messages(viber_request.sender.id,[TextMessage(text='Это картинка')])
        elif isinstance(viber_request, ViberSubscribedRequest):
            print(viber_request)
            # k=viber_request
            # print(type(k))
            f = open('static/Subscriber.txt', 'a')
            f.write('timestamp=' + str(viber_request.timestamp) + '\nUserProfile' + str(viber_request.user) +'\n')
            f.close()
            viber.send_messages(viber_request.user.id,[TextMessage(text='Приветствую тебя юный хоббит!!!')])
        elif isinstance(viber_request, ViberUnsubscribedRequest):
            f = open('static/UnSubscriber.txt', 'a')
            f.write('timestamp=' + str(viber_request.timestamp) + '\nuser_id=' + viber_request.user_id +'\n')
            f.close()
            # print(viber_request)
            # k=viber_request
            # print(type(k))
    return HttpResponse(status=200)


# token 4a863da4a227d272-425a6b66b594bba-a077ad6679ad30a  URI unicornservice
