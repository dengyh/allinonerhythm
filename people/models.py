# -*- coding: utf-8 -*-
from django.db import models
from team.models import Team

# Create your models here.

class Coach(models.Model):
	name = models.CharField(u'中文名', max_length = 32)
	EnglishName = models.CharField(u'外文名', max_length = 32)
	birth = models.DateField(u'出生日期', blank = True, null = True)
	picture = models.ImageField(u'头像', upload_to = 'coach', blank = True, null = True)
	country = models.CharField(u'国籍', max_length = 32)
	team = models.ForeignKey(Team, verbose_name = u'国家队')
	support = models.IntegerField(u'支持数', default = 0)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "教练"
		verbose_name_plural = "教练"

class Footballer(models.Model):
	name = models.CharField(u'中文名', max_length = 32)
	EnglishName = models.CharField(u'英文名', max_length = 32)
	position = models.CharField(u'位置', max_length = 32)
	birth = models.DateField(u'出生日期', blank = True, null = True)
	picture = models.ImageField(u'头像', upload_to = 'footballer', blank = True, null = True)
	club = models.CharField(u'效力俱乐部', max_length = 32)
	times = models.IntegerField(u'国家队出场次数', default = 0)
	team = models.ForeignKey(Team, verbose_name = u'国家队')
	support = models.IntegerField(u'支持数', default = 0)

	attack = models.IntegerField(u'攻击', default = 0)
	defense = models.IntegerField(u'防御', default = 0)
	coordinate = models.IntegerField(u'配合', default = 0)
	fitness = models.IntegerField(u'身体状态', default = 0)
	spiritual = models.IntegerField(u'精神状态', default = 0)
	injuries = models.IntegerField(u'伤病程度', default = 0)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "运动员"
		verbose_name_plural = "运动员"