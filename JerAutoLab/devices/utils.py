import datetime

from django.forms import DateInput

# class DatePickerInput(DateInput):
#     input_type = 'date'
# from .models import ADC
# from .views import alteons_list
from django.db.models import Q

from .models import ADC
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from .views import alteons_list

def paginateAlteons(request, alt_list, results):
    page = request.GET.get('page')
    
    paginator = Paginator(alt_list, results)
    try:
        alt_list = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        alt_list = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        alt_list = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, alt_list


def paginateRouters(request, router_list, results):
    page = request.GET.get('page')

    paginator = Paginator(router_list, results)
    try:
        router_list = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        router_list = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        router_list = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, router_list

def search(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print('SEARCH:', search_query)
    alteons_list = ADC.objects.filter(Q(Platform__icontains=search_query) | Q(RAM__icontains=search_query) | Q(Management__icontains=search_query))
    return alteons_list, search_query

# def reset_password(alteon):
#     alteon.Console:alteon.Management_Port



# def deleteAlteon(pk):
#     print('~~~~~~~~~~~~~~~~~~~~~ DELETE_ALTEON: ' ,request)
#     alteon = ADC.objects.get(id=pk)
#
#     # message = 'Are you sure?'
#     if request.method == 'POST':
#         alteon.delete()
#     return 'Delete Success'
    # context = {'alteon': alteon}
    # return render(request, 'devices/delete-alteon.html', context)


