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
from Products.ECLecture.Extensions.Migrations import migrate

def install(self, reinstall=False):
    """
    Installs the product.
    """
    out = StringIO()

    # Run migrations
    #if RUN_MIGRATIONS:
    print >> out, migrate(self)

    print >> out, "Successfully installed %s." % PRODUCT_NAME
    return out.getvalue()