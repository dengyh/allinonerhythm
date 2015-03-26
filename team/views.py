# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from team.models import Team
from people.models import Footballer, Coach
from match.models import Match

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.template import RequestContext

import datetime
import json
import types
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def team_view(request, template_name):
	teams = Team.objects.all().order_by('group')
	now = datetime.datetime.now().year
	for team in teams:
		team.players = Footballer.objects.filter(team = team)
		for player in team.players:
			player.age = now - player.birth.year
		try:
			team.coach = Coach.objects.get(team = team)
		except:
			pass
	return render_to_response(template_name, {
		'teams' : teams,
		}, context_instance = RequestContext(request))

def add_support(request):
	if request.method == 'GET':
		add_type = request.GET.get('add_type', None)
		add_id = request.GET.get('add_id', None)
		if add_id and add_type:
			if add_type == 'team':
				team = Team.objects.get(id = add_id)
				team.support += 1
				team.save()
				now_support = team.support
			elif add_type == 'coach':
				coach = Coach.objects.get(id = add_id)
				coach.support += 1
				coach.save()
				now_support = coach.support
			elif add_type == 'player':
				player = Footballer.objects.get(id = add_id)
				player.support += 1
				player.save()
				now_support = player.support
			return HttpResponse(json.dumps({
				'now_support' : now_support,
				'message' : 'success',
				}))
	return HttpResponse(json.dumps({
		'message' : 'faild',
		}))