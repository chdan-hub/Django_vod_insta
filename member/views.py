from django.shortcuts import render
from django.views.generic import FormView

from member.forms import SignUpForm


class SignupView(FormView):
    template_name = 'auth/signup.html'
    form_class = SignUpForm
