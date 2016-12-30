from django.conf.urls import url
from .views import login_view,Register_view,Logout_view

app_name='Accounts'
urlpatterns = [
    url(r'^login/$',login_view,name="login"),
    url(r'^register/$',Register_view,name="register"),
    url(r'^logout/$',Logout_view,name="logout"),
    
]