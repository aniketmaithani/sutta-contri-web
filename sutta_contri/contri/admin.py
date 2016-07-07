# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import SuttaRequirement


class SuttaRequirementsAdmin(admin.ModelAdmin):

    '''
    Admin View For Member Of SuttaRequirements
    '''
    list_display = ('name', 'brand_of_cig', 'number_of_cig',
                    'money_given',)
    list_filter = ('name',)
    search_fields = ('name', 'brand_of_cig', 'money_given')


admin.site.register(SuttaRequirement, SuttaRequirementsAdmin)
