# -*- coding: utf-8 -*-
# $Id$
#
# Copyright (c) 2006-2008 Otto-von-Guericke-Universität Magdeburg
#
# This file is part of ECLecture.
#
# ECLecture is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as 
# published by the Free Software Foundation; either version 2 of the 
# License, or (at your option) any later version.
#
# ECLecture is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ECLecture; if not, write to the Free Software Foundation, 
# Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
__author__ = """Mario Amelung <mario.amelung@gmx.de>"""
__docformat__ = 'plaintext'

from Products.ATContentTypes.configuration.config import zconf

try: # New CMF 
    from Products.CMFCore import permissions
except: # Old CMF 
    from Products.CMFCore import CMFCorePermissions as permissions


# i18n 
I18N_DOMAIN = 'eduComponents'

# dependencies of products to be installed by quick-installer
DEPENDENCIES = ['DataGridField']

# supported mime types for textfields
#EC_MIME_TYPES = ('text/x-web-intelligent',)
EC_MIME_TYPES = zconf.ATDocument.allowed_content_types
#EC_MIME_TYPES = ('text/plain', 'text/structured', 'text/x-rst', 'text/x-web-intelligent', 'text/html', )

# default mime type for textfields
#EC_DEFAULT_MIME_TYPE = 'text/x-web-intelligent'
EC_DEFAULT_MIME_TYPE = zconf.ATDocument.default_content_type
#EC_DEFAULT_MIME_TYPE = 'text/plain'

# default output format of textfields
#EC_DEFAULT_FORMAT = 'text/html'
EC_DEFAULT_FORMAT = 'text/x-html-safe'
