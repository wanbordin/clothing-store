from django.db import models
from email.mime import image
from django import template
from django.conf import settings
from os import listdir
from os.path import isfile
from os.path import join as path_join
from random import choice

import os
import os.path
import datetime

# Create your models here.


class Category_Shirt(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class Plain_Color(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class Pattern(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class Product_List(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    GENDER_CHOICES = [
        ('male', 'ชาย ♂'),
        ('female', 'หญิง ♀'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    Size_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]
    size = models.CharField(max_length=20, choices=Size_CHOICES)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200, blank=True, null=True)
    plain_color = models.ForeignKey(Plain_Color, on_delete=models.CASCADE, blank=True, null=True)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE, blank=True, null=True) # ลวดลาย
    image_shirt = models.ImageField(upload_to='clothing_store/static/img/shirt/', default='default.png')
    def __str__(self):
        return str(self.name)

# class Order_List(models.Model):
#     def __str__(self):
#         return str(self.eng_name)


# ราคา = หมวดหมู่สินค้า ขนาด และเพศผู้สวมใส
# 1	Polka Dot	(โพลก้าดอท)
# 2	Gingham	(กิงแฮม)
# 3	Tartan	(ทาร์ทัน)
# 4	Stripe	(สไตรป์)
# 5	Pinstripe	(พินสไตรป์)
# 6	Houndstooth	(ฮาวส์ทูธ)
# 7	Chevron	(เชฟรอน)
# 8	Herringbone	(เฮอร์ริ่งโบน)
# 9	Argyle	(อาร์กายล์)
# 10	Paisley	(พาสลีย์)

# white
# brown
# green
# pink
# blue
# yellow
# red