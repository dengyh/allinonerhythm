from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('backend.views',
	url(r'^$', 'backend_view', {'template_name' : 'backend.html'}),
)
