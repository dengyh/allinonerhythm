from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('myuser.views',
	url(r'login/$', 'login_view', {'template_name' : 'login.html'}),
	url(r'logout/$', 'logout_view', {'template_name' : 'logout.html'}),
	url(r'regist/$', 'register_view', {'template_name' : 'regist.html'}),
)
