# -*- coding: utf-8 -*-
from . import models
from rest_framework import serializers


class SuttaRequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SuttaRequirement
        fields = ('name', 'brand_of_cig', 'number_of_cig', 'money_given',)
