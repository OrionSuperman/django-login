from django.conf.urls import patterns, url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	url(r'^login/', views.Login.as_view(), name='accounts-login'),
	url(r'^register/', views.Register.as_view(), name='accounts-register'),
	url(r'^logout/$', views.Logout.as_view(), name='accounts-logout'),
	url(r'^success/', login_required(views.Success.as_view(), login_url='/accounts/login/'), name='accounts-success'),
)