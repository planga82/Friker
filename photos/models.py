# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGHT,'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creativecommons')
)

class photo(models.Model):

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True,null=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)

    def __unicode__(self):
        return self.name

