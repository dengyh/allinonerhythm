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
import types
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def players_view(request, template_name):
	teams = Team.objects.all().order_by('group')
	now = datetime.datetime.now().year
	for team in teams:
		team.players = Footballer.objects.filter(team = team)
		for player in team.players:
			player.age = now - player.birth.year
	return render_to_response(template_name, {
		'teams' : teams,
		}, context_instance = RequestContext(request))

def player_detail(request, player_id, template_name):
	player = Footballer.objects.get(id = player_id)
	return render_to_response(template_name, {
		'player' : player,
		}, context_instance = RequestContext(request))

def coach_view(request, template_name):
	coaches = Coach.objects.all().order_by('team')
	now = datetime.datetime.now().year
	for coach in coaches:
		coach.age = now - coach.birth.year
	return render_to_response(template_name, {
		'coaches' : coaches,
		}, context_instance = RequestContext(request))