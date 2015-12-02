from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$',
        views.UserProfileDetail.as_view(),
        name='user_profile_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        views.UserProfileUpdate.as_view(),
        name='user_profile_edit'),


]