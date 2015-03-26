from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('team.views',
	url(r'$', 'team_view', {'template_name' : 'team.html'}),
)
