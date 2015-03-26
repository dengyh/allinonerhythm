# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Team(models.Model):
	name = models.CharField(u'名称', max_length = 32, unique = True)
	EnglishName = models.CharField(u'英文名', max_length = 32)
	introduction = models.TextField(u'介绍')
	is_finalist = models.BooleanField(u'是否进入淘汰赛', default = False)
	logo = models.ImageField(u'队徽', upload_to = 'logo', blank = True, null = True)
	picture = models.ImageField(u'国旗', upload_to = 'team', blank = True, null = True)
	clothes = models.ImageField(u'队服', upload_to = 'clothes', blank = True, null = True)
	integration = models.IntegerField(u'小组赛积分', default = 0)
	support = models.IntegerField(u'支持数', default = 0)
	group = models.CharField(u'小组', max_length = 16, choices = (
		('A', u'A组'),
		('B', u'B组'),
		('C', u'C组'),
		('D', u'D组'),
		('E', u'E组'),
		('F', u'F组'),
		('G', u'G组'),
		('H', u'H组'),
	))

	attack = models.IntegerField(u'攻击', default = 0)
	defense = models.IntegerField(u'防守', default = 0)
	coordinate = models.IntegerField(u'配合', default = 0)
	fitness = models.IntegerField(u'力量', default = 0)
	speed = models.IntegerField(u'速度', default = 0)
	skill = models.IntegerField(u'技术', default = 0)
	spiritual = models.IntegerField(u'总体精神状态', default = 0)
	injuries = models.IntegerField(u'总体伤病情况', default = 0)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "球队"
		verbose_name_plural = "球队"