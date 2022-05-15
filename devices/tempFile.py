import datetime
from django.views import generic
import requests
from django.core import serializers
from django.db.models import Q
from django.core.management import sql
# from wtforms.fields import form
from ast import literal_eval
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import os
from django import template

register = template.Library()

from requests.auth import HTTPBasicAuth
# from urllib3.util import url

from .alteonRestAPI import check_usgae_days, restGetbuild, restGetRequest, restGetForm
from .models import ADC, Router

from .forms import *
# from .utils import search

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import serializers


@api_view(['GET'])
def apiOverview(request):
    alteons = ADC.objects.all()
    # for alteon in alteons:
    alteon = alteons[0]
    an_apiview = restGetRequest(alteon.Management, alteon.User_name, alteon.Password)
    return Response(an_apiview)

def update_alteon(request, pk):
    alteon = ADC.objects.get(MAC=pk)
    alteon_form = AlteonForm(instance=alteon)

    if request.method == 'POST':
        alteon_form = AlteonForm(request.POST, request.FILES, instance=alteon)  # initial=data
        alteon_form.MAC = pk
        # print(alteon_form.MAC)
        if alteon_form.is_valid():
            print("rr")
            alteon_form.save()
            return redirect('altlist')
        else:
            print("error")
    # date = get_date(alteon.Usage_Days)
    display = ['Platform', 'Owner', 'Console', 'Management', 'management port', 'Management Vlan', 'router management',
               'vlans', 'user name', 'password', 'usage days', 'notes']
    context = {'alteon_form': alteon_form, 'display': display}
    return render(request, "devices/edit_alteon.html", context)  # + date




class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [restGetRequest('172.185.150.2', 'admin', 'admin')]
        return Response({'an_apiview': an_apiview})

    def post(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.date)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, )


import sqlite3

database = "/Users/yonatank/OneDrive - Radware LTD/Jerlab/jerusalemlab.dc.sqlite3"
#########################################
# https://docs.python.org/3/library/sqlite3.html
# create a database connection
con = sqlite3.connect(database)


# cursor = con.execute("select * from ADC")

#
# for row in cursor.fetchall():
#     print('{0} : {1}'.format(row[9], row[1]))
#     ip = row[9]
#     platform = row[1]
#     previous_state = row[19]
#     print (previous_state)
#     version= restGetRequest(ip,'Version', 'admin', 'admin')
#     if version == "No Response":
#         state = "Unavailable"
#         if (previous_state == "Available"):
#             cursor.execute('''UPDATE ADC set State =?
#             Where Management = ?''',(state,ip))
#             con.commit()
#
#     else:
#         state = "Available"
#     if version != "401" and version != "No Response":
#         form= restGetRequest(ip, 'Form', 'admin', 'admin')
#         last_activity = restGetRequest(ip, 'LastApplyTime', 'admin', 'admin')
#         last_activity = last_activity[12:]
#         if platform != "4408":
#             build = restGetbuild(ip, 'admin', 'admin')
#             print (build)
#         else:
#             build = "unknown"
#         sslchip_text= restGetRequest(ip, 'SSLChip', 'admin', 'admin')
#         ram = restGetRequest(ip, 'RamSize', 'admin', 'admin')
#         print (ram)
#
#         if ("SSL Chip Type" in sslchip_text):
#             sc = (sslchip_text.split("SSL Chip Type: ",1)[1])
#             sslchip = sc.split(";",2)[0]
#         elif ("non-XL" in sslchip_text):
#             sslchip = "Non-XL"
#     if version !="401" and version !="No Response":
#         cursor.execute('''UPDATE ADC set Version = ?, Form = ?, 'SSL Card' = ?, 'LastApply' = ?, State =?, 'RAM' = ?, 'Build' = ?
#         Where Management = ?''',(version,form,sslchip,last_activity,state,ram,build,ip))
#         con.commit()
#     else:
#         print ("not updating the database")

##############################33


# Create your views here.
def home(request):
    alt_list = ADC.objects.all()
    return render(request, 'main.html')


def get_date(addDays=0, dateFormat="%d-%m-%Y"):
    # alt = Date_usage
    # addDays = ADC.Usage_Days
    timeNow = datetime.date.today()
    # test:###
    # if (addDays!=0):
    #     lastTime = timeNow + datetime.timedelta(days=addDays)
    #     days = str( lastTime - timeNow)
    #     return days[:days.find('d')]
    #####
    lastTime = timeNow + datetime.timedelta(days=addDays)
    return addDays


#############################################################################################

def create_alteon(request):
    alteon_form = AlteonForm()
    if request.method == 'POST':
        alteon_form = AlteonForm(request.POST, request.FILES)
        if alteon_form.is_valid():
            alteon_form.save()
            return redirect('altlist')
    display = ['mac', 'Platform', 'Owner', 'Console', 'Management', 'management port', 'Management Vlan',
               'router management', 'vlans', 'user name', 'password', 'usage days', 'notes']
    context = {'alteon_form': alteon_form, 'display': display}
    return render(request, "devices/Alteon_form.html", context)


#########################################################################################
def update_alteon(request, pk):
    alteon = ADC.objects.get(MAC=pk)
    alteon_form = AlteonForm(instance=alteon)

    if request.method == 'POST':
        alteon_form = AlteonForm(request.POST, request.FILES, instance=alteon)  # initial=data
        alteon_form.MAC = pk
        # print(alteon_form.MAC)
        if alteon_form.is_valid():
            print("rr")
            alteon_form.save()
            return redirect('altlist')
        else:
            print("error")
    # date = get_date(alteon.Usage_Days)
    display = ['Platform', 'Owner', 'Console', 'Management', 'management port', 'Management Vlan', 'router management',
               'vlans', 'user name', 'password', 'usage days', 'notes']
    context = {'alteon_form': alteon_form, 'display': display}
    return render(request, "devices/edit_alteon.html", context)  # + date


# class update_alteon(generic.CreateView):
#     model = ADC
#     fields = '__all__'
#     template_name = "devices/Alteon_form.html"
#     success_url = redirect('altlist')


#######################################################################
@register.simple_tag
def delete_alteon(request, pk):
    alteon = ADC.objects.get(MAC=pk)
    if request.method == 'POST':
        alteon.delete()
        return redirect('altlist')
    context = {'alteon': alteon}
    # return render(request, 'devices/delete-alteon.html', context)
    return render(request, 'devices/alteons_list.html', context)


# def alteon_details(alteon_id):
#     ref = alteon_id
#     my_adc = ADC.query.filter_by(MAC=ref).first()
#     my_alteon_ports = Alteon_ports.query.filter_by(alteon_id=ref).all()
#     my_detailed_alteon_ports = Alteon_ports.query.filter_by(alteon_id=ref).join(Router_ports).join(Router).all()
#     return render_template("alteon_details.html", my_adc=my_adc, my_ports=my_alteon_ports,
#                            my_detailed_alteon_ports=my_detailed_alteon_ports)

def projects(request):
    # projects = ADC.objects.get(Platform="6420")
    projects = ADC.objects.all()
    projects.map()
    context = {'projects': projects}

    return render(request, 'devices/alteon_details.html', context)
    # return render(request, 'devices/alteon_details.html')


def project(request, pk):
    projectObj = None
    # for i in projectList:
    #     if i['MAC'] == pk:
    #         projectObj = i
    # # return HttpResponse('Here are single project' + ' ' + str(pk))
    # alteon = ADC.objects.get(MAC=pk)
    # first_date = alteon.Date_usage
    return render(request, 'devices/routers_list.html', {'project': projectObj})
    # return render(request, 'devices/alteons_list.html', {'project': projectObj})


# @api_view(['GET'])
def alteon_details(request, pk):
    print(request)
    alteon = ADC.objects.get(MAC=pk)
    alteon_form = AlteonForm(instance=alteon)
    return_val = {'status_code': '', 'data': ''}
    params = ""
    # res = ""
    try:
        res = requests.get('https://{}/'.format(alteon.Management),
                           params=params,
                           auth=HTTPBasicAuth(alteon.User_name, alteon.Password),
                           verify=False,
                           allow_redirects=True)
        print(res.status_code)
    except:
        alteon.State = 'Unavailable - no Connection'
        print("connection error check device")
    if res.status_code == 200:
        print('yonatan')
        an_apiview = restGetRequest(alteon.Management, alteon.User_name, alteon.Password)
        # alteon.Version = restGetbuild(alteon.Management, alteon.User_name, alteon.Password)
        print(an_apiview)
        alteon.Version = an_apiview['Version']
        alteon.Form = an_apiview['Form']
        alteon.SSL_Card = an_apiview['SSLChip'].split(';')[1][
                          an_apiview['SSLChip'].split(';')[1].find(':') + 1:]
        alteon.RAM = an_apiview['RamSize']
        alteon.State = 'Available'
    # except:
    #     alteon.State = 'Unavailable - no Connection'
    #     print("connection error check device")

    ######################
    # if alteon.Usage_Days == 0 or alteon.Usage_Days is None:
    #     alteon.Usage_Days = 'Free to use'
    # elif alteon.Usage_Days > 0:
    #     firstTime = alteon.Date_usage
    #     timeNow = datetime.date.today()
    #     lastTime = firstTime + datetime.timedelta(alteon.Usage_Days)
    #     if lastTime > firstTime:
    #         days = str(lastTime - timeNow)
    #         days = days[:days.find('d')]
    #         # alteons[alteon.MAC] = days
    #         alteon.Usage_Days = days
    # days = check_usgae_days(alteon)
    print(check_usgae_days(alteon))
    print(alteon.Version)
    alteon.save()
    ######################
    # context = {'alteon': alteon, 'usafe_days': days}
    context = {'alteon': alteon}
    return render(request, "devices/alteon_details.html", context)


def alteons_list(request):
    alt_list, search_query = search(request)
    # alteons = {}

    # for alteon in alt_list:
    #     check_usgae_days(alteon)
    #     alteon.Version = restGetbuild(alteon.Management, alteon.User_name, alteon.Password)
    #     alteon.Form = restGetForm(alteon.Management, alteon.User_name, alteon.Password)

    ############################################
    # alteon_device_details = restGetRequest(alteon.Management, request, alteon.User_name, alteon.Password)
    # print(type(alteon_device_details))
    # alteon_device_details1 = dict(alteon_device_details)
    # # alteon.Version = alteon_device_details['Version']
    # alteon.Form = alteon_device_details['Form']
    # alteon.SSL_Card = alteon_device_details['SSLChip']
    ####################################################
    #     if alteon.Usage_Days == 0 or alteon.Usage_Days is None:
    #         alteon.Usage_Days = 'Free to use'
    #     elif alteon.Usage_Days > 0:
    #         firstTime = alteon.Date_usage
    #         timeNow = datetime.date.today()
    #         lastTime = firstTime + datetime.timedelta(alteon.Usage_Days)
    #         if lastTime > firstTime:
    #             days = str(lastTime - timeNow)
    #             days = days[:days.find('d')]
    #             # alteons[alteon.MAC] = days
    #             alteon.Usage_Days = days

    # for alteon in alt_list:
    #     days = get_date(alteon.Usage_Days)
    #     alteons[alteon.MAC] = days
    context = {'alt_list': alt_list}
    return render(request, 'devices/alteons_list.html', context)


##########################################3
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
    context = {'router_list': router_list}

    return render(request, 'devices/routers_list.html', context)


def edit_router(request, pk):
    router = Router.objects.get(Management=pk)
    router_form = RouterForm(instance=router)

    if request.method == 'POST':
        router_form = RouterForm(request.POST, request.FILES, instance=router)  # initial=data
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


# def usage_calculator(request, pk):
#     # adc = ADC.objects.get(MAC = pk)
#     # usage = datetime.timedelta #alteon.Usage_Days
#     use = update_alteon(request, pk).date
#     print(use)
# usage = adc.Usage_Days
# if usage > 0:

# def clean_sku(alteon_form):
#     if alteon_form.instance:
#         context = {'alteon_form': alteon_form}
#         return context
#     else:
#         return alteon_form.fields['__all__']

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class SignUpView(CreateView):
    template_name = 'devices/signup.html'
    form_class = UserCreationForm
