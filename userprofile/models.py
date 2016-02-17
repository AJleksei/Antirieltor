# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    email = models.EmailField()
    avatar = models.FilePathField(path=PROJECT_PATH + '/account/images')
    # Поле заполняется автоматически при создании объекта
    register_date = models.DateTimeField(auto_now_add=True)
    """

    user = models.OneToOneField(User)
    latest_editing = models.DateTimeField(auto_now=True)
    test_name = models.CharField(max_length=30, default='')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
