# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import settings

from django.template import RequestContext
#from sae.mail import send_mail

def index_view(request, template_name):
	return render_to_response(template_name, {}, context_instance = RequestContext(request))

def privacy_view(request, template_name):
	return render_to_response(template_name, {}, context_instance = RequestContext(request))

@csrf_exempt
def mail_view(request, template_name):
	message = None
	flag = None
	if request.method == 'POST':
		title = request.POST.get('title', None)
		body = request.POST.get('body', None)
		print title
		print body
		if title and body:
			#send_mail(settings.EMAIL_ADMIN, title, body,
			#	(settings.EMAIL_HOST, settings.EMAIL_PORT,
			#		settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD,
			#		settings.EMAIL_USE_TLS))
			send_mail('dengyh7@qq.com', title, body,('smtp.qq.com', 25, 'dengyh7@qq.com', '~,heng~,3986366', False))
			message = '发送成功'
			flag = True
		else:
			message = '发送失败'
			flag = False
	return render_to_response(template_name, {
		'message' : message,
		'flag' : flag,
		}, context_instance = RequestContext(request))
