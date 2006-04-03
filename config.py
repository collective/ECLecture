# -*- coding: utf-8 -*-
# $Id$
#
# Copyright (c) 2006 Otto-von-Guericke-Universität Magdeburg
#
# This file is part of ECLecture.

from Products.CMFCore import permissions

GLOBALS = globals()

I18N_DOMAIN = 'eduComponents'

# define skins directory
SKINS_DIR = 'skins'

# define dependencies
#DEPENDENCIES = ['Archetypes', 'DataGridField', 'AddRemoveWidget', 'intelligenttext']
DEPENDENCIES = ['Archetypes', 'DataGridField']

# define product and tool names
PRODUCT_NAME = 'ECLecture'

ECL_NAME = 'ECLecture'
ECL_TITLE = 'Lecture'
ECL_META = ECL_NAME
ECL_ICON = 'folder_icon.gif'
#ECL_ICON = 'folder-16.png'

# define permissions
add_permission  = permissions.AddPortalContent
edit_permission = permissions.ModifyPortalContent
view_permission = permissions.View

# define text types
TEXT_TYPES = (
    'text/structured',
    'text/x-rst',
    'text/html',
    'text/plain',
    )

# some LOG levels
BLATHER=-100
DEBUG=-200
TRACE=-300
