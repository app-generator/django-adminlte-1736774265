# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customer(models.Model):

    #__Customer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    domain = models.CharField(max_length=255, null=True, blank=True)
    services = models.CharField(max_length=255, null=True, blank=True)
    m365_tenant_id = models.CharField(max_length=255, null=True, blank=True)
    m365_client_id = models.CharField(max_length=255, null=True, blank=True)
    m365_client_secret = models.CharField(max_length=255, null=True, blank=True)
    ninja_orgid = models.IntegerField(null=True, blank=True)
    acronis_tenant_id = models.CharField(max_length=255, null=True, blank=True)
    acronis_client_id = models.CharField(max_length=255, null=True, blank=True)
    acronis_client_secret = models.CharField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Productmapping(models.Model):

    #__Productmapping_FIELDS__
    license_sku_id = models.CharField(max_length=255, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    license_part_number = models.CharField(max_length=255, null=True, blank=True)

    #__Productmapping_FIELDS__END

    class Meta:
        verbose_name        = _("Productmapping")
        verbose_name_plural = _("Productmapping")


class Service(models.Model):

    #__Service_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Service_FIELDS__END

    class Meta:
        verbose_name        = _("Service")
        verbose_name_plural = _("Service")


class Licenserecord(models.Model):

    #__Licenserecord_FIELDS__
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    sku_id = models.CharField(max_length=255, null=True, blank=True)
    total_licenses = models.IntegerField(null=True, blank=True)
    used_licenses = models.IntegerField(null=True, blank=True)
    retrieved_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Licenserecord_FIELDS__END

    class Meta:
        verbose_name        = _("Licenserecord")
        verbose_name_plural = _("Licenserecord")


class Setting(models.Model):

    #__Setting_FIELDS__
    key = models.CharField(max_length=255, null=True, blank=True)
    value = models.TextField(max_length=255, null=True, blank=True)

    #__Setting_FIELDS__END

    class Meta:
        verbose_name        = _("Setting")
        verbose_name_plural = _("Setting")



#__MODELS__END
