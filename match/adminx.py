# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction

from match.models import Match, Video, Ball, Shop

class MatchAdmin(object):
    list_display = ('id', 'team_one', 'team_two', 'winner', 'state', 'location', 'datetime')

class VideoAdmin(object):
    list_display = ('id', 'title', 'type', 'url', 'match')

class BallAdmin(object):
    list_display = ('id', 'name')

class ShopAdmin(object):
    list_display = ('id', 'name', 'balls')

xadmin.site.register(Match, MatchAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(Ball, BallAdmin)
xadmin.site.register(Shop, ShopAdmin)