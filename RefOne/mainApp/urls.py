from django.conf.urls import url
from mainApp import views

# TEMPLATE URLS!
app_name = 'mainApp'

urlpatterns = [
    url(r'^signup', views.signup, name='signup'),
    url(r'^user_login', views.user_login, name='user_login'),
    url(r'^$', views.SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
]
