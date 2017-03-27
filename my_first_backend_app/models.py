from __future__ import unicode_literals

import uuid

from django.utils.datetime_safe import datetime

# Create your models here.

from mongoengine import *


def create_hash(*args, **kwargs):
    return uuid.uuid4().hex[0:30]

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    username = StringField(max_length=30, default=create_hash)
    password = StringField(max_length=200, required=True)

