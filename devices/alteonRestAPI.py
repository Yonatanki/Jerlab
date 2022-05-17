'''
@author: Yonatan Kim
'''
from ast import literal_eval
import requests
from requests import auth
from requests.exceptions import ConnectionError
from requests.auth import HTTPBasicAuth
import sqlite3 as sql
import json
from .models import *
from textwrap import indent
import time
import threading

UPDATE_INTERVAL = 21600

# Alteon_rest = {'Version': 'agSoftwareVersion', 'Form': 'agFormFactor', 'SSLChip': 'hwSslChipInfo',
#                'LastApplyTime': 'agSwitchLastApplyTime', 'LastSaveTime': 'agSwitchLastSaveTime', 'RamSize': 'ramSize', 'Platform': 'agPlatformIdentifier', 'MAC': 'hwMACAddress' }

Alteon_rest = {'Version': 'agSoftwareVersion', 'Form': 'agFormFactor', 'SSLChip': 'hwSslChipInfo', 'RamSize': 'ramSize', 'Platform': 'agPlatformIdentifier', 'MAC': 'hwMACAddress' }


##############################################
####### convert_byte_to_string  ##############
##############################################
def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    elif isinstance(data, dict):
        return dict(map(convert, data.items()))
    elif isinstance(data, tuple):
        return map(convert, data)
    else:
        return data


########################################################
#######  Rest API Get an Alteon Request   ##############
########################################################
def restGetRequest(ip, user, psw):
    alteon_data_dict = {}
    for alt_rest_key, value in Alteon_rest.items():

        try:
            rest = requests.get('https://{}/config?prop={}'.format(ip, value), auth=HTTPBasicAuth(user, psw),
                                verify=False, timeout=5)
        except:
            print("No Response")
            return "No Response"
        if rest.status_code == 401:
            return 401
        dic0 = convert(rest.content)
        dic1 = literal_eval(dic0)
        for key, value1 in dic1.items():
            if key == value:
                # return value1
                alteon_data_dict.update({alt_rest_key: value1})
    return alteon_data_dict


def restGetRequest1(ip, request, user, psw):
    for key, value in Alteon_rest.items():
        if key == request:
            try:
                rest = requests.get('https://{}/config?prop={}'.format(ip, value), auth=HTTPBasicAuth(user, psw),
                                    verify=False, timeout=5)
            except ConnectionError as e:
                print("No Response")
                return "No Response"
            if rest.status_code == 401:
                return "401"
            dic0 = convert(rest.content)
            dic1 = literal_eval(dic0)
            for key, value1 in dic1.items():
                if key == value:
                    return value1


########################################################
#######  Rest API Get an Alteon build   ##############
########################################################

def restGetbuild(ip, user, psw):
    try:
        rest = requests.get('https://{}/config/AgImageAdcTable?props=Version,Status'.format(ip),
                            auth=HTTPBasicAuth(user, psw), verify=False, timeout=7)
    except ConnectionError as e:
        return "unknown2"
    if rest.status_code == 401:
        return "unknown1"
    dic0 = convert(rest.content)
    dic1 = literal_eval(dic0)
    list1 = dic1.get('AgImageAdcTable')
    for item in list1:
        if item.get('Status') == 1:
            return item.get('Version')
    return 'unknown'


########################################################
#######  Rest API Get an Alteon Form   ##############
########################################################

def restGetForm(ip, user, psw):
    try:
        rest = requests.get('https://{}/config/agFormFactor?props=Version,Status'.format(ip),
                            auth=HTTPBasicAuth(user, psw), verify=False, timeout=5)
        print(rest)
        time.sleep(0.5)
    except ConnectionError as e:
        return "unknown"
    if rest.status_code == 401:
        return "unknown"
    dic0 = convert(rest.content)
    dic1 = literal_eval(dic0)
    list1 = dic1.get('agFormFactor')
    # for item in list1:
    #     if item.get('Status') == 1:
    return list1


########################################################
#######  Rest API Apply Configuration   ################
########################################################

def restApply(ip, user, psw):
    try:
        rest = requests.get('https://{}/monitor?prop=agApplyPending'.format(ip), auth=HTTPBasicAuth(user, psw),
                            verify=False, timeout=3)
    except ConnectionError as e:
        return "unknown"
    if rest.status_code == 401:
        return "unknown"
    dic0 = convert(rest.content)
    dic1 = literal_eval(dic0)
    if dic1.get('agApplyPending') == 2:
        try:
            rest1 = requests.post('https://{}/config?action=apply'.format(ip), auth=HTTPBasicAuth(user, psw),
                                  verify=False, timeout=3)
        except ConnectionError as e:
            return "unknown"
        if rest1.status_code == 401:
            return "unknown"
        dic2 = convert(rest1.content)
        dic3 = literal_eval(dic2)
        return "new configuration applied"
    else:
        return "Apply operation not needed"


########################################################
#######  Rest API Configure NTP Server    ##############
########################################################

def restNTPServer(ip, user, psw):
    timeZone = "agNewDaylightSavings"
    enable = "agNewCfgNTPService"
    primary_IP_Address = "agNewCfgNTPServer"
    secondary_IP_Address = "agNewCfgNTPSecServer"
    synchronization_Interval = "agNewCfgNTPResyncInterval"
    timezone_Offset = "agNewCfgNTPTzoneHHMM"
    payload = {
        timeZone: "206",
        enable: "1",
        primary_IP_Address: "216.239.35.0",
        secondary_IP_Address: "216.239.35.4",
        synchronization_Interval: "10",
        timezone_Offset: "+00:00"
    }
    try:
        rest = requests.put('https://{}/config'.format(ip), data=json.dumps(payload, indent=4),
                            auth=HTTPBasicAuth(user, psw), verify=False, timeout=3)
    except ConnectionError as e:
        return "unknown"
    if rest.status_code == 401:
        return "unknown"
    dic0 = convert(rest.content)
    dic1 = literal_eval(dic0)
    if dic1.get('status') == 'ok':
        return "Success"
    else:
        return "Failure"


##############################################
#######  main   ##############
##############################################
requests.packages.urllib3.disable_warnings()


# database = "/root/PycharmProjects/myautomatedlab/project/mylab1.db"
# create a database connection
# con = sql.connect(database)

# all_ADCs = ADC.objects.all()


# for this_adc in all_ADCs:
#     ip = this_adc.Management
#     platform = this_adc.Device_Name
#     previous_state = this_adc.LastApply
#
#     version = restGetRequest(ip, 'Version', 'admin', 'admin')
#     if version == "No Response":
#         state = "Unavailable"
#         if (previous_state == "Available"):
#             this_adc.State = state
#             db.session.add(this_adc)
#             db.session.commit()
#
#     else:
#         state = "Available"
#
#     if version != "401" and version != "No Response":
#         form = restGetRequest(ip, 'Form', 'admin', 'admin')
#         last_activity = restGetRequest(ip, 'LastApplyTime', 'admin', 'admin')
#         last_activity = last_activity[12:]
#         if platform != "4408":
#             build = restGetbuild(ip, 'admin', 'admin')
#         else:
#             build = "unknown"
#         sslchip_text = restGetRequest(ip, 'SSLChip', 'admin', 'admin')
#         ram = restGetRequest(ip, 'RamSize', 'admin', 'admin')
#
#         if ("SSL Chip Type" in sslchip_text):
#             sc = (sslchip_text.split("SSL Chip Type: ", 1)[1])
#             sslchip = sc.split(";", 2)[0]
#         elif ("non-XL" in sslchip_text):
#             sslchip = "Non-XL"
#     if version != "401" and version != "No Response":
#         this_adc.Version = version
#         this_adc.Form = form
#         this_adc.SSL_Card = sslchip
#         this_adc.LastApply = last_activity
#         this_adc.State = state
#         this_adc.RAM = ram
#         this_adc.Build = build
#         print(this_adc.Version, this_adc.Form, this_adc.SSL_Card, this_adc.LastApply, this_adc.State, this_adc.RAM,
#               this_adc.Build)
#
#         # cursor.execute('''UPDATE Alteons set Version = ?, Form = ?, 'SSL Card' = ?, 'LastApply' = ?, State =?, 'RAM' = ?, 'Build' = ?
#         # Where Management = ?''',(version,form,sslchip,last_activity,state,ram,build,ip))
#         db.session.add(this_adc)
#         db.session.commit()
#         # con.commit()
#     else:
#         print("not updating the database")


def check_usgae_days(alteon):
    '''the function gets Alteon and count the reamainig days to use from submited date from.'''
    if alteon.Usage_Days == 0 or alteon.Usage_Days is None:
        return 0
    # elif alteon.Usage_Days > 0:
    firstTime = alteon.Date_usage
    timeNow = datetime.date.today()
    lastTime = firstTime + datetime.timedelta(alteon.Usage_Days)
    print('First time saved: ', firstTime)
    print('The device in use until: ', lastTime)
    
    print(lastTime-timeNow)
    print(lastTime - firstTime, 'test')
    print(timeNow-timeNow, 'sedasd')
    if lastTime > firstTime:
        days = str(lastTime - firstTime)
        print(days)
        days = days[:days.find('d')]

        alteon.Usage_Days = int(days)
        print(alteon.Usage_Days)
        alteon.save()
        return alteon.Usage_Days

#
# def update_currencies_at_interval(interval=UPDATE_INTERVAL):
#     '''  update the currency depending on interval in seconds
#          default value is 6 hours (21600 seconds)
#     '''
#     assert isinstance(interval, int), f'check interval setting {interval} must be an integer'
#
#     wtd = WorldTradingData()
#     wtd.setup()
#     start_time = time.time()
#     current_time = start_time
#     elapsed_time = int(current_time - start_time)
#
#     while True:
#         if elapsed_time % interval == 0:
#             wtd.update_currencies()
#
#         current_time = time.time()
#         elapsed_time = int(current_time - start_time)
#
#
# thread_update_currencies = threading.Thread(
#     target=update_currencies_at_interval, kwargs={'interval': UPDATE_INTERVAL})
# thread_update_currencies.start()
