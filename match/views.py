# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from team.models import Team
from people.models import Footballer, Coach
from match.models import Match, Video

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.template import RequestContext

import datetime
import json
import types
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')

def bubble_sort(sort_list):
	iter_len = len(sort_list)
	if iter_len < 2:
		return sort_list
	for i in range(iter_len - 1):
		for j in range(iter_len - i - 1):
			if sort_list[j].datetime > sort_list[j + 1].datetime:
				sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
	return sort_list

class Group:
	def __init__(self, name, list):
		self.name = name + '组'
		self.list = bubble_sort(list)

def match_view(request, template_name):
	matches = Match.objects.all().order_by('datetime').order_by('group')
	groups = []
	flag = ''
	now = 0
	nowTime = datetime.datetime.now()
	endTime = nowTime - datetime.timedelta(0, 6500)
	for match in matches:
		matchTime = match.datetime.replace(tzinfo = None) + datetime.timedelta(0, 28800)
		if matchTime > nowTime:
			match.state = 'notStart'
			match.save()
			match.flag = '还未开始'
		elif matchTime < endTime:
			match.state = 'end'
			match.save()
			match.flag = '已经结束'
		else:
			print matchTime
			print endTime
			print nowTime
			match.state = 'now'
			match.save()
			match.flag = '正在进行'
		match.collection = Video.objects.filter(match = match).filter(type = 'collection')
		match.direct = Video.objects.filter(match= match).filter(type = 'direct')
		if len(match.direct) > 0:
			match.hasMatch = True
		else:
			match.hasMatch = False
		if flag != match.group:
			flag = match.group
			groups.append(Group(flag, matches[now:now+6]))
			now += 6
	return render_to_response(template_name, {
		'groups' : groups,
		}, context_instance = RequestContext(request))

class TestTeam:
	def __init__(self, team):
		self.name = team.name
		self.attack = team.attack
		self.defense = team.defense
		self.coordinate = team.coordinate
		self.fitness = team.fitness
		self.speed = team.speed
		self.skill = team.skill
		self.score = 0
		self.goal = 0
		self.goaled = 0
		self.grade = (self.attack * 200 + self.defense * 250 + self.speed * 120 + self.skill * 150 + self.fitness * 100 + self.coordinate * 180) * 100 / 26 - 253846

class Simulation:
	def __init__(self, teamA, teamB, teamAs, teamBs, winner):
		self.teamA = teamA
		self.teamB = teamB
		self.teamAs = teamAs
		self.teamBs = teamBs
		self.winner = winner

	def run(self):
		if not self.winner:
			scoreA = self.teamA.grade
			scoreB = self.teamB.grade
			testA = scoreA * random.randint(0, 10000)
			testB = scoreB * random.randint(0, 10000)
			defer = abs(scoreA - scoreB)
			draw = (45000 / defer + 4) * 10000000
			if testA >= testB:
				if testA - testB < draw:
					self.winner = None
					self.teamAs, self.teamBs = getScore(scoreA, scoreB, True)
				else:
					self.winner = self.teamA
					self.teamAs, self.teamBs = getScore(scoreA, scoreB, False)
			else:
				if testB - testA < draw:
					self.winner = None
					self.teamAs, self.teamBs = getScore(scoreA, scoreB, True)
				else:
					self.winner = self.teamB
					self.teamBs, self.teamAs = getScore(scoreB, scoreA, False)
		return (self.teamA.name + " " + str(self.teamAs) + " - " + str(self.teamBs) + " " + self.teamB.name, self.winner, self.teamAs, self.teamBs)

def getScore(temp1, temp2, flag):
	weight1 = [20, 50, 80, 92, 98, 100]
	weight2 = [15, 42, 75, 90, 98, 100]
	weight3 = [12, 37, 72, 88, 96, 100]
	weight4 = [8, 28, 66, 86, 95, 100]
	weight5 = [3, 18, 54, 84, 94, 100]
	defer = temp1 - temp2
	if defer < 20000:
		score1 = getRandomGoal(flag, weight1)
	elif defer < 40000:
		score1 = getRandomGoal(flag, weight2)
	elif defer < 60000:
		score1 = getRandomGoal(flag, weight3)
	elif defer < 80000:
		score1 = getRandomGoal(flag, weight4)
	else:
		score1 = getRandomGoal(flag, weight5)
	if flag:
		score2 = score1
	else:
		score2 = random.randint(0, score1 - 1)
	return (score1, score2)

def getRandomGoal(flag, weight):
	if flag:
		num = random.randint(0, 100)
	else:
		num = random.randint(weight[0], 100)
	for i in xrange(5):
		if num < weight[i]:
			return i
	return 5

def getPlayoffTeam(group):
	teamA = TestTeam(group[0])
	teamB = TestTeam(group[1])
	teamC = TestTeam(group[2])
	teamD = TestTeam(group[3])
	messages = []
	teamA, teamB, message = getResult(teamA, teamB)
	messages.append(message)
	teamC, teamD, message = getResult(teamC, teamD)
	messages.append(message)
	teamA, teamC, message = getResult(teamA, teamC)
	messages.append(message)
	teamB, teamD, message = getResult(teamB, teamD)
	messages.append(message)
	teamA, teamD, message = getResult(teamA, teamD)
	messages.append(message)
	teamB, teamC, message = getResult(teamB, teamC)
	messages.append(message)
	return getRank(teamA, teamB, teamC, teamD), messages

def getRank(teamA, teamB, teamC, teamD):
	first = teamA
	second = None
	third = None
	fourth = None
	if compareTeam(teamB, first):
		second = first
		first = teamB
	else:
		second = teamB
	if compareTeam(teamC, first):
		third = second
		second = first
		first = teamC
	elif compareTeam(teamC, second):
		third = second
		second = teamC
	else:
		third = teamC
	if compareTeam(teamD, first):
		fourth = third
		third = second
		second = first
		first = teamD
	elif compareTeam(teamD, second):
		fourth = third
		third = second
		second = teamD
	elif compareTeam(teamD, third):
		fourth = third
		third = teamD
	else:
		fourth = teamD
	return first, second, third, fourth

def compareTeam(teamA, teamB):
	if teamA.score > teamB.score:
		return True
	elif teamA.score == teamB.score and (teamA.goal - teamA.goaled) > (teamB.goal - teamB.goaled):
		return True
	elif teamA.score == teamB.score and (teamA.goal - teamA.goaled) == (teamB.goal - teamB.goaled) and (teamA.goal > teamB.goal):
		return True
	return False

def getResult(teamA, teamB):
	match = Simulation(teamA, teamB, 0, 0, None)
	result, winner, goalA, goalB = match.run()
	teamA.goal += goalA
	teamB.goaled += goalA
	teamA.goaled += goalB
	teamB.goal += goalB
	if winner == teamA:
		teamA.score += 3
	elif winner == teamB:
		teamB.score += 3
	else:
		teamA.score += 1
		teamB.score += 1
	return teamA, teamB, result

def getWinner(teamA, teamB):
	match = Simulation(teamA, teamB, 0, 0, None)
	result, winner, goalA, goalB = match.run()
	if winner == None:
		testA = teamA.score * random.randint(0, 10000)
		testB = teamB.score * random.randint(0, 10000)
		if testA > testB:
			result += " (" + teamA.name + "点球胜)"
			return teamA, result
		else:
			result += " (" + teamB.name + "点球胜)"
			return teamB, result
	return winner, result

def getWinnerAndLoser(teamA, teamB):
	winner, result = getWinner(teamA, teamB)
	if winner == teamA:
		return teamA, teamB, result
	else:
		return teamB, teamA, result

def simulation_game(request ,template_name):
	teams = Team.objects.all().order_by('group')
	groupA = teams[0:4]
	groupB = teams[4:8]
	groupC = teams[8:12]
	groupD = teams[12:16]
	groupE = teams[16:20]
	groupF = teams[20:24]
	groupG = teams[24:28]
	groupH = teams[28:32]
	# print "------------GroupA---------------"
	tot = 0
	for x in xrange(10000):
		(A1, A2, A3, A4), ResultA = getPlayoffTeam(groupA)
		if A1.attack == 87 or A2.attack == 87:
			tot += 1
	print tot
	# print "------------GroupB---------------"
	(B1, B2, B3, B4), ResultB = getPlayoffTeam(groupB)
	# print "------------GroupC---------------"
	(C1, C2, C3, C4), ResultC = getPlayoffTeam(groupC)
	# print "------------GroupD---------------"
	(D1, D2, D3, D4), ResultD = getPlayoffTeam(groupD)
	# print "------------GroupE---------------"
	(E1, E2, E3, E4), ResultE = getPlayoffTeam(groupE)
	# print "------------GroupF---------------"
	(F1, F2, F3, F4), ResultF = getPlayoffTeam(groupF)
	# print "------------GroupG---------------"
	(G1, G2, G3, G4), ResultG = getPlayoffTeam(groupG)
	# print "------------GroupH---------------"
	(H1, H2, H3, H4), ResultH = getPlayoffTeam(groupH)
	# print "------------Sixteen--------------"
	Result16 = []
	W49, result = getWinner(A1, B2)
	Result16.append(result)
	W50, result = getWinner(C1, D2)
	Result16.append(result)
	W51, result = getWinner(B1, A2)
	Result16.append(result)
	W52, result = getWinner(D1, C2)
	Result16.append(result)
	W53, result = getWinner(E1, F2)
	Result16.append(result)
	W54, result = getWinner(G1, H2)
	Result16.append(result)
	W55, result = getWinner(F1, E2)
	Result16.append(result)
	W56, result = getWinner(H1, G2)
	Result16.append(result)
	# print "------------Eight----------------"
	Result8 = []
	W57, result = getWinner(W49, W50)
	Result8.append(result)
	W58, result = getWinner(W53, W54)
	Result8.append(result)
	W59, result = getWinner(W51, W52)
	Result8.append(result)
	W60, result = getWinner(W55, W56)
	Result8.append(result)
	# print "------------Four-----------------"
	Result4 = []
	W61, L61, result = getWinnerAndLoser(W57, W58)
	Result4.append(result)
	W62, L62, result = getWinnerAndLoser(W59, W60)
	Result4.append(result)
	# print "------------Final----------------"
	W63, L63, Third = getWinnerAndLoser(L61, L62)
	W64, L64, Final = getWinnerAndLoser(W61, W62)
	return render_to_response(template_name, {
		'ResultA' : ResultA,
		'ResultB' : ResultB,
		'ResultC' : ResultC,
		'ResultD' : ResultD,
		'ResultE' : ResultE,
		'ResultF' : ResultF,
		'ResultG' : ResultG,
		'ResultH' : ResultH,
		'Result16' : Result16,
		'Result8' : Result8,
		'Result4' : Result4,
		'Third' : Third,
		'Final' : Final,
		}, context_instance = RequestContext(request))