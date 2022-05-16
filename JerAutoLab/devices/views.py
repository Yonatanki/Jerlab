from django.contrib import messages

from . import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime
from django.views import generic
import requests

# from django.contrib import messages
from django.db.models import Q
from django.core.management import sql
# from wtforms.fields import form
from ast import literal_eval
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import os

from requests.auth import HTTPBasicAuth
# from urllib3.util import url

from .alteonRestAPI import check_usgae_days, restGetbuild, restGetRequest, restGetForm
from .models import ADC, Router

from .forms import *
from .utils import search, paginateAlteons, paginateRouters

from django import template
register = template.Library()


# Create your views here.
def home(request):
    # alt_list = ADC.objects.all()
    return render(request, 'main.html')

# def home(request):
#     # alt_list = ADC.objects.all()
#     if request.is_ajax():
#         ser = serializers.serialize('json')
#         return render(request, 'main.html')


def get_date(addDays=0, dateFormat="%d-%m-%Y"):
    timeNow = datetime.date.today()
    lastTime = timeNow + datetime.timedelta(days=addDays)
    return addDays


#############################################################################################

def create_alteon(request):
    alteon_form = AlteonForm()
    if request.method == 'POST':
        alteon_form = AlteonForm(request.POST, request.FILES)

        if alteon_form.is_valid():
            print('Valid')

            alteon_form.save()
            alteon = alteon_form.save(commit=False)

            messages.info(request, 'Alteon successfully added')
            print(alteon)

            return redirect('altlist')
        
        else:
            errors =  alteon_form._errors
            messages.info(request, errors)        

    display = ['Owner', 'Console', 'Management', 'management port', 'Management Vlan',
               'router management', 'vlans', 'user name', 'password', 'usage days', 'notes']
    context = {'alteon_form': alteon_form, 'display': display}
    return render(request, "devices/Alteon_form.html", context)


#########################################################################################
def update_alteon(request, pk):

    alteon = ADC.objects.get(id=pk)
    alteon_form = AlteonForm(instance=alteon)

    if request.method == 'POST':

        alteon_form = AlteonForm(
            request.POST, request.FILES, instance=alteon)  # initial=data

        if alteon_form.is_valid():
   
            alteon_form.save()
            messages.success(request, 'Alteon details updated successfully.')
            return redirect('alteon-details', pk=pk)
        else:
            messages.success(request, 'Alteon details updated usuccessfull.')

    display = ['Platform', 'Owner', 'Console', 'Management', 'management port', 'Management Vlan',
               'router management', 'vlans', 'user name', 'password', 'usage days', 'notes']
    context = {'alteon_form': alteon_form, 'display': display}
    return render(request, "devices/edit_alteon.html", context)  # + date

#######################################################################


# @register.simple_tag
def delete_alteon(request, pk):
    alteon = ADC.objects.get(id=pk)
    # message = 'Are you sure?'
    if request.method == 'POST':
        alteon.delete()
        return redirect('altlist')
    context = {'alteon': alteon}
    return render(request, 'devices/delete-alteon.html', context)
    # return render(request, context)


# @api_view(['GET'])
def alteon_details(request, pk):
    print(request)
    alteon = ADC.objects.get(id=pk)
    alteon_form = AlteonForm(instance=alteon)
    context = {'alteon': alteon}
    # alteon.get_alteon_form
    alteon.get_days
    # check_usgae_days(alteon)
    return_val = {'status_code': '', 'data': ''}
    print('Usage Days', alteon.Usage_Days)
    alteon.save()
    return render(request, "devices/alteon_details.html", context)


def alteons_list(request):
    alt_list, search_query = search(request)
    custom_range, alt_list = paginateAlteons(request, alt_list, 10)
    # print('USAGE DAYS:', alt_list[0].Usage_Days)
    print('USAGE DAYS:', alt_list)
    # print(paginator.page_range)
    # alteons = ADC.objects.all()
    # for alteon in alteons:
    #     an_apiview = restGetRequest(alteon.Management, alteon.User_name, alteon.Password)
    #     print(an_apiview)
    # alteon.RAM = an_apiview['RamSize']
    context = {'alt_list': alt_list, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'devices/alteons_list.html', context)

# 3
# request should be ajax and method should be POST.
#     if request.is_ajax and request.method == "POST":
#         # get the form data
#         form = AlteonForm(request.POST)
#         # save the data and after fetch the object in instance
#         if form.is_valid():
#             instance = form.save()
#             # serialize in new friend object in json
#             ser_instance = serializers.serialize('json', [ instance, ])
#             # send to client side.
#             return JsonResponse({"instance": ser_instance}, status=200)
#         else:
#             # some form errors occured.
#             return JsonResponse({"error": form.errors}, status=400)
#
#     # some error occured
#     return JsonResponse({"error": ""}, status=400)


def create_router(request):
    router_form = RouterForm()
    if request.method == 'POST':
        router_form = RouterForm(request.POST)
        if router_form.is_valid():
            # temp = router_form.cleaned_data.get("Management")
            # print(temp)
            router_form.save()
            return redirect('routers_list')
        else:
            return render(request, "devices/Router_form.html", router_form.errors.as_data())

    context = {'router_form': router_form}
    return render(request, "devices/Router_form.html", context)


def routers_list(request):
    # router_list, search_query = search(request)
    router_list = Router.objects.all()
    custom_range, router_list = paginateRouters(request, router_list, 10)
    context = {'router_list': router_list, 'custom_range': custom_range}

    return render(request, 'devices/routers_list.html', context)


def edit_router(request, pk):
    router = Router.objects.get(Management=pk)
    router_form = RouterForm(instance=router)

    if request.method == 'POST':
        router_form = RouterForm(
            request.POST, request.FILES, instance=router)  # initial=data
        router_form.id = pk
        # print(router_form.Management)
        if router_form.is_valid():
            # print("rr")
            router_form.save()
            return redirect('routers_list')
        else:
            print("error")
    # date = get_date(alteon.Usage_Days)
    # display = ['Platform', 'Owner', 'Console', 'Management', 'management port', 'Management Vlan', 'router management',
    #            'vlans', 'user name', 'password', 'usage days', 'notes']
    context = {'router_form': router_form}
    return render(request, "devices/Router_form.html", context)


def delete_router(request, pk):
    router = Router.objects.get(id=pk)
    if request.method == 'POST':
        router.delete()
        return redirect('routers_list')
    context = {'router': router}
    return render(request, 'devices/delete-alteon.html', context)




############################### Test ########################
def postContact(request):
    if request.method == "POST" and request.is_ajax():
        form = AlteonForm(request.POST)
        form.save()
        return JsonResponse({"success": True}, status=200)
    return JsonResponse({"success": False}, status=400)


@api_view(['GET'])
def apiOverview(request):
    alteons = ADC.objects.all()
    for alteon in alteons:

        an_apiview = restGetRequest(
            alteon.Management, alteon.User_name, alteon.Password)
    return Response(an_apiview)
