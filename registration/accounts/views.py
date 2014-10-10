from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from accounts.forms import UserRegistrationForm
from accounts.models import Avatar

@csrf_exempt
def register(request):
    if(request.method == 'POST'):
        form = UserRegistrationForm(request.POST, request.FILES)
        if(form.is_valid()):
            if(User.objects.filter(Q(username = form.cleaned_data['username']) | Q(email = form.cleaned_data['email'])).count() != 0):
                return HttpResponseBadRequest("An account with this username or email already exists.")
            else:
                user = User(username = form.cleaned_data['username'], email = form.cleaned_data['email'])
                user.set_password(form.cleaned_data['password'])
                user.save()
                if(form.cleaned_data['avatar'] != None):
                    avatar = Avatar(user = user, avatar_image = form.cleaned_data['avatar'])
                    avatar.save()
                return HttpResponse()
        else:
            return HttpResponseBadRequest("There was something wrong with the information you inputed: %s" % form.errors) 
    else:
        return HttpResponseBadRequest("This endpoint does not support any method other than POST.")


