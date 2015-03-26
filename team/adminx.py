# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction

from team.models import Team

class TeamAdmin(object):
	list_display = ('id', 'name', 'introduction', 'integration', 'is_finalist')

xadmin.site.register(Team, TeamAdmin)