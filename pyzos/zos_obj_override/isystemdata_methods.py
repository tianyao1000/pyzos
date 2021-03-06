# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        isystemdata_methods.py
# Purpose:     store custom methods for wrapper class of ISystemData Interface 
# Licence:     MIT License
#-------------------------------------------------------------------------------
"""Store custom methods for wrapper class of ISystemData Interface, which provides
   Interfaces and methods for changing all System Explorer data. This interface 
   can be accessed via the IOpticalSystem interface. 
   name := repr(zos_obj).split()[0].split('.')[-1].lower() + '_methods.py' 
"""
from __future__ import print_function
from __future__ import division
from win32com.client import CastTo as _CastTo, constants as _constants
from pyzos.zosutils import wrapped_zos_object as _wrapped_zos_object


# Overridden properties
# ---------------------

# Extra methods
# -------------


# Extra properties
# ----------------
