# -*- coding: utf-8 -*-
# $Id$
#
# Copyright (c) 2006 Otto-von-Guericke-Universität Magdeburg
#
# This file is part of ECLecture.

from StringIO import StringIO

from Products.Archetypes.Extensions.utils import installTypes, install_subskin
from Products.Archetypes.public import listTypes
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility

from Products.GenericSetup.interfaces import ISetupTool 

EXTENSION_PROFILES = ('Products.ECLecture:default',) 

# local imports
from Products.ECLecture.config import *
from Products.ECLecture.Extensions.Migrations import migrate

def install(self, reinstall=False):
    """
    Installs the product.
    """
    out = StringIO()
	# If the config contains a list of dependencies, try to install
    # them.  Add a list called DEPENDENCIES to your custom
    # AppConfig.py (imported by config.py) to use it.
    try:
        from Products.ECLecture.config import DEPENDENCIES
    except:
        DEPENDENCIES = []
    portal = getToolByName(self,'portal_url').getPortalObject()
    quickinstaller = portal.portal_quickinstaller
    portal_setup = getToolByName(self, 'portal_setup')
    for dependency in DEPENDENCIES:
        print >> out, "Installing dependency %s:" % dependency
        quickinstaller.installProduct(dependency)
        transaction.commit(1)

    # Run migrations
    #if RUN_MIGRATIONS:
    # print >> out, migrate(self)
	# The following section is boilerplate code that can be reused when you 
    # need to invoke a GenericSetup profile from Install.py. 
	for extension_id in EXTENSION_PROFILES: 
		portal_setup.setImportContext('profile-%s' % extension_id) 
		portal_setup.runAllImportSteps(purge_old=False) 
		product_name = extension_id.split(':')[0] 
		quickinstaller.notifyInstalled(product_name) 
	 	transaction.savepoint()
	
    print >> out, "Successfully installed %s." % PRODUCT_NAME
    return out.getvalue()