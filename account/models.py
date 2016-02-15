# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class account(models.Model):
    login = models.CharField(max_length=50)
    # Поле будет хешироваться (длины 50 может быть мало)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    # Поле заполняется автоматически при создании объекта
    register_date = models.DateTimeField(auto_now_add=True)
