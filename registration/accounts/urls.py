from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^register/$', views.register, name="register")
]