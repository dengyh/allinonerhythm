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

from django.template import RequestContext

import datetime
import types
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@csrf_exempt
def login_view(request, template_name):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	next_page = request.GET.get('next_page', '')
	login_message = ''

	if request.method == 'POST':
		next_page = request.POST.get('next_page', '')
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username = username, password = password)
		if user is None:
			login_message = '用户不存在'
		elif not user.is_active:
			login_message = '用户无效'
		else:
			auth.login(request, user)
			login_message = '登录成功'
			return HttpResponseRedirect(next_page)

	return render_to_response(template_name, {
		'next_page' : next_page,
		'login_message' : login_message
		}, context_instance = RequestContext(request))

def logout_view(request, template_name):
	auth.logout(request)
	return HttpResponseRedirect('/')

@csrf_exempt
def register_view(request, template_name):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect('/user/login/')
	else:
		form = UserCreationForm()
	return render_to_response(template_name, {'form' : form})
