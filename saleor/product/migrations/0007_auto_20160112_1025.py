# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("product", "0006_product_updated_at")]

    operations = [migrations.RenameModel("FixedProductDiscount", "Discount")]
