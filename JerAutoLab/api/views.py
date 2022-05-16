# from django.http import JsonResponse
from rest_framework.decorators import api_view
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ADCSerializer
from devices.models import ADC, Router
# from devices.utils import deleteAlteon

import requests
from requests.auth import HTTPBasicAuth

# from django.http.HttpRequest
from devices.alteonRestAPI import restGetRequest


# Alteon_rest = {'Version': 'agSoftwareVersion', 'Form': 'agFormFactor', 'SSLChip': 'hwSslChipInfo',
#                'LastApplyTime': 'agSwitchLastApplyTime', 'LastSaveTime': 'agSwitchLastSaveTime', 'RamSize': 'ramSize', 'Platform': 'agPlatformIdentifier'}


@api_view(['GET', 'POST'])
def getRoutes(request):
    routes = [
        {'GET': '/api/alteons-list'},
        {'GET': '/api/alteon-details/id'},
        {'POST': '/api/alteon-details/id/'},

        # {'POST': '/api/users/token'},
        # {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def getHome(request):
    print('Home Page')
    alt_list = ADC.objects.all()
    serializer = ADCSerializer(alt_list, many=True)
    # print('Serializer: ', serializer.data)

    # for alteon in serializer.data:
    for alteon in alt_list:
        print('Alteon: ', alteon)
        getAlteonRestApi(alteon)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def getAlteonsList(request):
    print('USER111:', request.user)
    alt_list = ADC.objects.all()
    serializer = ADCSerializer(alt_list, many=True)
    # print('Serializer: ', serializer.data)

    # for alteon in serializer.data
    # for alteon in alt_list:
    #     getAlteonRestApi(alteon)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def getAlteonDetail(request, pk):
    alteon = ADC.objects.get(id=pk)
    print('api_view_getAlteonDetail function')
    getAlteonRestApi(alteon)
    # res = restGetRequest(alteon.Management, alteon.User_name, alteon.Password)
    serializer = ADCSerializer(alteon, many=False)
    # serializer1 = ADCSerializer(res, many=False)
    # print(res)
    return Response(serializer.data)


@api_view(['POST','DELETE', 'GET'])
def postDeleteAlteon(request, pk):
    print('************************* REQUEST: ', request)
    alteon = ADC.objects.get(id=pk)
    serializer = ADCSerializer(alteon, many=False)
    if request == 'POST':
        deleteAlteon(pk)
    return Response(serializer.data)


# @api_view(['GET', 'POST'])
def getAlteonRestApi(alteon):
    # alteon = ADC.objects.get(MAC=pk)
    try:
        an_apiview = restGetRequest(
            alteon.Management, alteon.User_name, alteon.Password)

        if an_apiview != 'No Response' or an_apiview != 401:
            print('Res: ', an_apiview)
            alteon.MAC = an_apiview['MAC']
            alteon.Version = an_apiview['Version']
            alteon.RAM = an_apiview['RamSize']
            alteon.Platform = an_apiview['Platform']
            alteon.State = 'Online'
            alteon.Form = an_apiview['Form']
            SSL_Card = an_apiview['SSLChip'].split(';')
            print('SSL_Card: ', SSL_Card)
            nonXL = str(SSL_Card).find('non-XL')
            if nonXL > -1:
                alteon.SSL_Card = 'non-XL'
            else:
                alteon.SSL_Card = SSL_Card[1][SSL_Card[1].find(':') + 1:]
            # alteon.SSL_Card = an_apiview['SSLChip'].split(';')
            alteon.save()
    except:
        alteon.State = 'Offline - no Connection'
        alteon.save()
        print('RESULTS:    ', an_apiview)
        return
    # context = {'alteon': alteon, 'Json': JsonResponse(an_apiview)}
    print('############################### Alteon Rest API DONE #################################')
    return Response(an_apiview)

# ##############################################
# ####### convert_byte_to_string  ##############
# ##############################################
# def convert(data):
#     if isinstance(data, bytes):
#         return data.decode('ascii')
#     elif isinstance(data, dict):
#         return dict(map(convert, data.items()))
#     elif isinstance(data, tuple):
#         return map(convert, data)
#     else:
#         return data


# ########################################################
# #######  Rest API Get an Alteon Request   ##############
# ########################################################

# def restGetRequest(ip, user, psw):
#     alteon_data_dict = {}
#     for alt_rest_key, value in Alteon_rest.items():

#         try:
#             rest = requests.get('https://{}/config?prop={}'.format(ip, value), auth=HTTPBasicAuth(user, psw),
#                                 verify=False, timeout=5)
#         except ConnectionError as e:
#             print("No Response")
#             return "No Response"
#         if rest.status_code == 401:
#             return "401"
#         dic0 = convert(rest.content)
#         dic1 = literal_eval(dic0)
#         for key, value1 in dic1.items():
#             if key == value:
#                 # return value1
#                 alteon_data_dict.update({alt_rest_key: value1})
#     return alteon_data_dict
