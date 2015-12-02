from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from .models import UserProfile, assure_user_profile_exists

class UserProfileDetail(DetailView):
    model = UserProfile

class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = ('homepage',)

    def get(self, request, *args, **kwargs):
        assure_user_profile_exists(kwargs['pk'])
        return (super(UserProfileUpdate, self).
                get(self, request, *args, **kwargs))
