# -*- coding: utf-8 -*-
# $Id$
#
# Copyright (c) 2006 Otto-von-Guericke-Universität Magdeburg
#
# This file is part of ECLecture.

from zLOG import LOG, INFO

LOG('ECLecture', INFO, 'Installing Product')

import os, os.path

from Globals import package_home

from Products.Archetypes.public import process_types, listTypes
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory

# local imports
from Products.ECLecture.config import *


registerDirectory(SKINS_DIR, GLOBALS)

def initialize(context):
    """
    """
    # Import Types here to register them
    from Products.ECLecture import content

    from AccessControl import ModuleSecurityInfo
    from AccessControl import allow_module, allow_class, allow_type

    content_types, constructors, ftis = process_types(
        listTypes(PRODUCT_NAME),
        PRODUCT_NAME)
    
    utils.ContentInit(
        PRODUCT_NAME + ' Content',
        content_types      = content_types,
        permission         = add_permission,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)
