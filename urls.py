from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import xadmin
import settings
xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.registe_models()

urlpatterns = patterns('',
	url(r'^team/$', 'team.views.team_view', {'template_name' : 'team.html'}),  
	url(r'^support/$', 'team.views.add_support'),                 
	url(r'^match/$', 'match.views.match_view', {'template_name' : 'match.html'}),
	url(r'^coach/$', 'people.views.coach_view', {'template_name' : 'coach.html'}),
	url(r'^players/$', 'people.views.players_view', {'template_name' : 'players.html'}),
	url(r'^player/(\d+)/$', 'people.views.player_detail', {'template_name' : 'player.html'}),
	url(r'^user/', include('myuser.urls')),
	url(r'^backend/', include('backend.urls')),
	url(r'^xadmin/', include(xadmin.site.urls)),
	url(r'^mail/$', 'index.views.mail_view', {'template_name' : 'contact.html'}),
	url(r'^simulation/$', 'match.views.simulation_game', {'template_name' : 'simulation.html'}),
	url(r'^$', 'index.views.index_view', {'template_name' : 'index.html'}),
	url(r'^privacy/$', 'index.views.privacy_view', {'template_name' : 'privacy.html'}),
	url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_PATH}), 
)

