# -*- coding: utf-8 -*-
# $Id$
#
# Copyright (c) 2006-2009 Otto-von-Guericke-Universität Magdeburg
#
# This file is part of ECLecture.
#
__author__ = """Mario Amelung <mario.amelung@gmx.de>"""
__docformat__ = 'plaintext'

import re

try:
    from Products.validation.interfaces.IValidator import IValidator
except ImportError:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
    from interfaces.IValidator import IValidator
    del sys, os


class TimePeriodValidator:
    """
    Ensure that we don't get a value for start and/or end time of a time period
    which are not valid.
    """
    __implements__ = IValidator

    def __init__(self, name, title='', description=''):
        self.name = name
        self.title = title or name
        self.description = description
    
    def __call__(self, value, *args, **kwargs):
        """
        """
        if value[0] or value[1]:

            for item in value:
                m = re.match('^\s*(\d\d)[.:]?(\d\d)\s*$', item)
    
                if not m:
                    return ("Validation failed: '%(value)s' is not a time specification." %
                            { 'value': item, })
        
        return True
