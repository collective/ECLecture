# -*- coding: utf-8 -*-
# $Id$
#
# Copyright (c) 2006 Otto-von-Guericke-Universit�t Magdeburg
#
# This file is part of ECLecture.
#
# ECAssignmentBox is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# ECAssignmentBox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ECAssignmentBox; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from AccessControl import ClassSecurityInfo

from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName

from Products.Archetypes.public import DisplayList
from Products.Archetypes.public import Schema
from Products.Archetypes.public import TextField
from Products.Archetypes.public import StringField
from Products.Archetypes.public import DateTimeField
from Products.Archetypes.public import IntegerField
from Products.Archetypes.public import StringWidget
from Products.Archetypes.public import RichWidget
from Products.Archetypes.public import CalendarWidget
from Products.Archetypes.public import SelectionWidget

from Products.ATContentTypes.configuration import zconf

from Products.ATContentTypes.content.base import registerATCT
from Products.ATContentTypes.content.base import updateActions, updateAliases

from Products.ATContentTypes.content.folder import ATFolderSchema
from Products.ATContentTypes.content.folder import ATFolder

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.DataGridField.DataGridField import DataGridField
from Products.DataGridField.DataGridWidget import DataGridWidget

# local imports
from Products.ECLecture.config import PRODUCT_NAME, ECL_NAME, ECL_TITLE, ECL_META, ECL_ICON, I18N_DOMAIN
from Products.ECLecture.TimePeriodField import TimePeriodField

# -- schema definition --------------------------------------------------------
ECLectureSchema = ATFolderSchema.copy() + Schema((

    StringField('joinURL',
        required = False,
        widget = StringWidget(
            label = "Registration link",
            description = """Link to the registration for this lecture""",
            label_msgid = 'label_join_url',
            description_msgid = 'help_join_url',
            size = 65,
            i18n_domain = I18N_DOMAIN,
        ),
    ),
                                                   
    
    TimePeriodField('timePeriod',
        accessor = 'getTimePeriod',
        edit_accessor = 'getTimePeriodForEdit',
        required = True,
        widget = StringWidget(
            macro = 'time_period',
            size = 5,
            maxlength = 5,
            label = "Time period",
            description = "",
            label_msgid = 'label_time_period',
            description_msgid = 'help_time_period',
            i18n_domain = I18N_DOMAIN,
        ),
    ),

    DateTimeField('startDate',
        required = True,
        widget = CalendarWidget(
            label = "Start date",
            description = "",
            label_msgid = 'label_start_date',
            description_msgid = 'help_start_date',
            show_hm = False, 
            #show_ymd = True,
            i18n_domain = I18N_DOMAIN,
        ),
    ),
    
    DateTimeField('endDate',
        required = True,
        widget = CalendarWidget(
            label = "End date",
            description = "",
            label_msgid = 'label_end_date',
            description_msgid = 'help_end_date',
            show_hm = False, 
            #show_ymd = True,
            i18n_domain = I18N_DOMAIN,
        ),
    ),
                                                   
    IntegerField('recurrence',
        vocabulary = 'getRecurrenceDisplayList',
        widget = SelectionWidget(
            format = "radio", # possible values: flex, select, radio
            label = "Recurrence",
            description = "",
            label_msgid = 'label_recurrence',
            description_msgid = 'help_recurrence',
            i18n_domain = I18N_DOMAIN,
        ),
    ),
                                                   
    StringField('room',
        required = True,
        widget = StringWidget(
            label = "Room",
            description = """Room for this lecture""",
            label_msgid = 'label_room',
            description_msgid = 'help_room',
            i18n_domain = I18N_DOMAIN,
        ),
    ),

    DateTimeField('firstSession',
        widget = CalendarWidget(
            label = "First session",
            description = """Date for the first session for this lecture""",
            label_msgid = 'label_first_session',
            description_msgid = 'help_first_session',
            #show_hm = False, 
            i18n_domain = I18N_DOMAIN,
        ),
    ),

    StringField('directoryEntry',
        required = False,
        widget = StringWidget(
            label = "Directory entry",
            description = """Link to the directory entry for this lecture""",
            label_msgid = 'label_directory_entry',
            description_msgid = 'help_directory_entry',
            size = 65,
            i18n_domain = I18N_DOMAIN,
        ),
    ),

    DataGridField('availableResources',
        default = ({'title':'Slides', 'url':'slides', 
                    'icon':'book_icon.gif'},                    
                   {'title':'Exercise', 'url':'exercise', 
                    'icon':'folder-box-16.png'},),
        widget=DataGridWidget(
            label="Available resources",
            description=""""Enter available resources for this lecture. Title 
is the name of a resource as shown to the user; URL must be a path inside this
site or an URL to an external source; Icon is optional.""",
            column_names=('Title', 'URL', 'Icon',),
            label_msgid='label_available_resourcess',
            description_msgid = 'help_available_resources',
            i18n_domain = I18N_DOMAIN,
        ),
        required = True,
        columns = ('title', 'url', 'icon')
    ),

    TextField('text',
        required=True,
        searchable=True,
        primary=True,
        #storage = AnnotationStorage(migrate=True),
        validators = ('isTidyHtmlWithCleanup',),
        #validators = ('isTidyHtml',),
        default_content_type = zconf.ATDocument.default_content_type,
        default_output_type = 'text/x-html-safe',
        allowable_content_types = zconf.ATDocument.allowed_content_types,
        widget = RichWidget(
            label = "Body Text",
            label_msgid = "label_body_text",
            description = "Enter lecture information",
            description_msgid = "help_body_text",
            rows = 18,
            i18n_domain = I18N_DOMAIN,
            allow_file_upload = zconf.ATDocument.allow_document_upload, 

        )
    ),

),)

finalizeATCTSchema(ECLectureSchema, folderish=True, moveDiscussion=False)


class ECLecture(ATFolder):
    """A folder which contains lecture information."""

    __implements__ = (ATFolder.__implements__)

    security       = ClassSecurityInfo()

    schema         =  ECLectureSchema


    content_icon   = ECL_ICON
    meta_type      = ECL_META
    portal_type    = ECL_META
    archetype_name = ECL_TITLE

    default_view   = 'ecl_view'
    immediate_view = 'ecl_view'

    #suppl_views    = ()

    # -- actions --------------------------------------------------------------
    aliases = updateAliases(ATFolder, {
        'view': 'ecl_view',
        })

    # -- methods --------------------------------------------------------------
    security.declarePrivate('getRecurrenceDisplayList')
    def getRecurrenceDisplayList(self):
        """
        Returns a display list of recurrence types.
        """
        dl = DisplayList(())
        
        dl.add(0, 'Daily')
        dl.add(1, 'Weekly')
        dl.add(2, 'Monthly')
        dl.add(3, 'Yearly')

        return dl


    def getTimePeriod(self):
        """
        @return a string representing a time period
        """
        value = self.getTimePeriodForEdit()
        return ' - '.join(value)


    def getTimePeriodForEdit(self):
        """
        @return a list with two values representing start and end time of a 
                time period
        """
        value = self.getField('timePeriod').get(self)
        result = []
        
        for item in value:
            result.append('%02d:%02d' % (item/60, item%60))
            
        return result


registerATCT(ECLecture, PRODUCT_NAME)
