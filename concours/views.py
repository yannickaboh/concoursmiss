from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.core.urlresolvers import reverse_lazy


from django.http import HttpResponseRedirect
from .models import Gprovince
from .filters import GprovinceFilter



# Create your views here.


def index(request):
	p_list = Gprovince.objects.all()
	p_filter = GprovinceFilter(request.GET, queryset=p_list)
	return render(request, 'concours/index.html', {'filter':p_filter})

def miss(request):
	return render(request, 'concours/miss.html', {})
