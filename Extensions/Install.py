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

# local imports
from Products.ECLecture.config import *

def installDependencies(self, out):
    """
    Checks wether or not depending products are installed. 
    If not, try to install them.
    """
    qi = getToolByName(self, 'portal_quickinstaller')
    for product in DEPENDENCIES:
        if (qi.isProductInstallable(product)) and (not qi.isProductInstalled(product)):
            qi.installProduct(product)


def setupTool(self, out):
    """ 
    Add the tool to the portal root folder.
    """
    pass

def removeTool(self):
    """
    Remove the tool from the portal root folder.
    """
    pass

def addPrefsPanel(self, out):
    """
    Add the tool to Plone's preferences panel.
    """
    pass


def removePrefsPanel(self):
    """
    Remove the tool from Plone's preferences panel.
    """
    pass
    

def setWorkflow(self, out):
    """
    Add workflow.
    """
    pass


def install(self):
    """
    Installs the product.
    """
    out = StringIO()

    # install depending products
    installDependencies(self, out)

    # install types
    installTypes(self, out, listTypes(PRODUCT_NAME), PRODUCT_NAME)

    # install subskins
    install_subskin(self, out, GLOBALS)

    # install workflows
    setWorkflow(self, out)

    # install tools
    setupTool(self, out)

    # register tool to preferences panel
    addPrefsPanel(self, out)

    print >> out, "Successfully installed %s." % PRODUCT_NAME
    return out.getvalue()


def uninstall(self):
    """ 
    Uninstalls the product.
    """
    out = StringIO()

    # remove tool from prefs panel
    removePrefsPanel(self)

    # remove tool from portal root
    removeTool(self)

    print >> out, "Successfully uninstalled %s." % PRODUCT_NAME
    return out.getvalue()
