from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index',views.index,name='index'),
    url(r'^login',views.login,name='login'),
    url(r'^home',views.home,name='home'),
    url(r'^signup',views.signup,name='signup'),



]