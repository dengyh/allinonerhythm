# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction

from people.models import Coach, Footballer
class CoachAdmin(object):
	list_display = ('id', 'name', 'EnglishName', 'birth', 'picture', 'team', 'country')

class FootballerAdmin(object):
	list_display = ('id', 'name', 'EnglishName', 'birth', 'picture',
		'club', 'times', 'team', 'support')

xadmin.site.register(Coach, CoachAdmin)
xadmin.site.register(Footballer, FootballerAdmin)