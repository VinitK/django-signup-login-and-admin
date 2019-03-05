from django.conf.urls import url
from mainApp import views

# TEMPLATE URLS!
app_name = 'mainApp'

urlpatterns = [
    url(r'^signup', views.signup, name='signup'),
    url(r'^user_login', views.user_login, name='user_login')
]