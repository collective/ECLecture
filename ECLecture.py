# -*- coding: utf-8 -*-
# $Id$
#
# Copyright (c) 2006 Otto-von-Guericke-Universit�t Magdeburg
#
# This file is part of ECLecture.

from AccessControl import ClassSecurityInfo

from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName

from Products.Archetypes.public import DisplayList
from Products.Archetypes.public import Schema
from Products.Archetypes.public import TextField
from Products.Archetypes.public import StringField
from Products.Archetypes.public import StringWidget
from Products.Archetypes.public import RichWidget

from Products.ATContentTypes.configuration import zconf

from Products.ATContentTypes.content.base import registerATCT
from Products.ATContentTypes.content.base import updateActions, updateAliases

from Products.ATContentTypes.content.folder import ATFolderSchema
from Products.ATContentTypes.content.folder import ATFolder

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.DataGridField.DataGridField import DataGridField
from Products.DataGridField.DataGridWidget import DataGridWidget

# local
from Products.ECLecture.config import PRODUCT_NAME, ECL_NAME, ECL_TITLE, ECL_META, ECL_ICON, I18N_DOMAIN

ECLectureSchema = ATFolderSchema.copy() + Schema((

    StringField('joinURL',
        required = False,
        widget = StringWidget(
            label = "Registration link",
            description = """Link to the registration for this lecture""",
            label_msgid = 'label_join_url',
            description_msgid = 'help_join_url',
            i18n_domain = I18N_DOMAIN,
        ),
    ),

    StringField('dateAndTime',
        required = True,
        widget = StringWidget(
            label = "Date/Time",
            description = """Date and time for this lecture""",
            label_msgid = 'label_date_time',
            description_msgid = 'help_date_time',
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

    StringField('directoryEntry',
        required = False,
        widget = StringWidget(
            label = "Directory entry",
            description = """Link to the directory entry for this lecture""",
            label_msgid = 'label_directory_entry',
            description_msgid = 'help_directory_entry',
            i18n_domain = I18N_DOMAIN,
        ),
    ),

    DataGridField('availableResources',
        default = ({'title':'Exercise', 'url':'exercise', 'icon':'folder-box-16.png'},),
        widget=DataGridWidget(
            label="Available resources",
            description="Enter available resources for this lecture",
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


registerATCT(ECLecture, PRODUCT_NAME)
