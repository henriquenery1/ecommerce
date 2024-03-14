from django.http import HttpResponse
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View

class HomePage(View):
    def get(self, request):
        return HttpResponse("Hello world!")