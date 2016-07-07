# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models


class SuttaRequirement(models.Model):
    name = models.CharField(blank=False, null=False, max_length=256)
    brand_of_cig = models.CharField(
        blank=False, null=False, max_length=100, help_text='Brand of the Cigg')
    number_of_cig = models.CharField(
        blank=False, null=False, max_length=100, help_text='Number of Cig you want to order')
    money_given = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sutta Requirement"
        verbose_name_plural = "Sutta Requirements"
        ordering = ['-name']
