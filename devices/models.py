import datetime

from django.db import models
import uuid

# from wtforms.widgets import DateInput
# from django.forms import DateInput

# from .utils import DatePickerInput
# Create your models here.
from django.db.models.signals import post_save, post_delete

from .alteonRestAPI import restGetbuild, check_usgae_days, restGetRequest, restGetForm


class ADC(models.Model):
    __tablename__ = "ADC"

    MAC = models.CharField(max_length=200, unique=True, null=True, blank=True)
    Platform = models.CharField(max_length=200, blank=True)
    # Rack = models.IntegerField(default=0)
    RAM = models.CharField(max_length=200, blank=True)
    SSL_Card = models.CharField(max_length=200, blank=True)
    Version = models.CharField(max_length=200, blank=True)
    Owner = models.EmailField(max_length=200)
    # em= models.EmailField()
    Management = models.CharField(max_length=200, unique=True)
    Console = models.CharField(max_length=200, blank=True)
    Management_Port = models.CharField(max_length=200, blank=True)
    Management_Vlan = models.CharField(max_length=200, blank=True)
    State = models.CharField(max_length=200, blank=True)
    Router_Management = models.ForeignKey(
        'Router', on_delete=models.CASCADE, null=True, blank=True)
    Vlans = models.CharField(max_length=200, blank=True)
    User_name = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Form = models.CharField(max_length=200, blank=True)
    Usage_Days = models.PositiveIntegerField(null=True, blank=True)
    Notes = models.CharField(max_length=200, null=True, blank=True)
    Date_usage = models.DateField(auto_now=True)
    # tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.Management

    class Meta:
        ordering = ['Management']


    @property
    def get_alteon_api(self):
        an_apiview = restGetRequest(
            self.Management, self.User_name, self.Password)
        print(an_apiview)
        self.Version = an_apiview['Version']
        self.Form = an_apiview['Form']
    
    @property
    def get_alteon_form(self):
        a = restGetForm(self.Management, self.User_name, self.Password)
        print('yonatan.......', a)
    # @property
    # def get_version(self):
    #     self.Version = restGetbuild(
    #         self.Management, self.User_name, self.Password)
    #     self.save()

    @property
    def get_days(self):
        self.Usage_Days = check_usgae_days(self)
        self.save()
    # def __init__(self, management):
    #     # self.MAC = mac
    #     # self.Platform = device_name
    #     # self.Rack = rack
    #     self.Management = management
        # self.Owner = username
        # self.Console = console_ip
        # self.State = console_port
        # self.Router_Management = router
        # self.Notes = notes

    # def __repr__(self):
    #     return '<{}>'.format(self.Version)


class Router(models.Model):
    __tablename__ = "Router"

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    Device_Name = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Management = models.GenericIPAddressField(max_length=200, unique=True, error_messages={
                                              'unique': "This IP has already been exist."})
    # Management = models.Man
    # Alteon_MAC = models.ForeignKey(to=ADC, on_delete=models.CASCADE)
    User_name = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Notes = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.Management
    # def __repr__(self):
    #     return '<Router {}>'.format(self.Device_Name)

# class Tag(models.Model):
#     name = models.CharField(max_length=200)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#
#     def __str__(self):
#         return self.name
