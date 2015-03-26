# -*- coding: utf-8 -*-
from django.db import models
from team.models import Team

# Create your models here.

class Match(models.Model):
	team_one = models.ForeignKey(Team, verbose_name = u'主队', related_name = 'team_one')
	team_two = models.ForeignKey(Team, verbose_name = u'客队', related_name = 'team_two')
	team_one_goal = models.IntegerField(u'主队进球数', default = 0)
	team_two_goal = models.IntegerField(u'客队进球数', default = 0)
	winner = models.ForeignKey(Team, verbose_name = u'胜者', blank = True, null = True, related_name = 'winner')
	state = models.CharField(u'比赛情况', max_length = 16, choices = (
		('now', u'正在进行'),
		('end', u'已经结束'),
		('notStart', u'还未开始'),
	))
	group = models.CharField(u'比赛类型', max_length = 16, choices = (
		('A', u'A组赛'),
		('B', u'B组赛'),
		('C', u'C组赛'),
		('D', u'D组赛'),
		('E', u'E组赛'),
		('F', u'F组赛'),
		('G', u'G组赛'),
		('H', u'H组赛'),
		('16', u'十六强赛'),
		('8', u'八强赛'),
		('4', u'半决赛'),
		('2', u'决赛'),
	))
	location = models.CharField(u'球场', max_length = 32)
	datetime = models.DateTimeField(u'比赛时间(北京时间)')

	def __unicode__(self):
		return self.team_one.name + 'VS' + self.team_two.name

	class Meta:
		verbose_name = "比赛"
		verbose_name_plural = "比赛"

class Video(models.Model):
	type = models.CharField(u'视频', max_length = 16, choices = (
		('direct', u'直播视频'),
		('collection', u'集锦视频'),
	))
	url = models.CharField(u'地址', max_length = 256)
	title = models.CharField(u'主题', max_length = 256)
	match = models.ForeignKey(Match)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = '视频'
		verbose_name_plural = '视频'

class Ball(models.Model):
	name = models.CharField(max_length = 32)

class Shop(models.Model):
	name = models.CharField(max_length = 32)
	balls = models.ManyToManyField(Ball)