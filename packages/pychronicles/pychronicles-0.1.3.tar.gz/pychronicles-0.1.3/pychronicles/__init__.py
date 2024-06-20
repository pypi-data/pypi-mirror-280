#!/bin/python3
# -*- coding: utf-8 -*-
"""
Chronicles package

@author: Thomas Guyet
@date: 10/2022
@institution: Inria
"""

name = "pychronicles"
__version__ = "0.1.1"

# load the essential classes
from pychronicles.timedsequence import TimedSequence
from pychronicles.chronicle import Chronicle
from pychronicles.fchronicle import FuzzyChronicle
from pychronicles.abstraction import Abstracter

# load the pandas accessors
import pychronicles.pandas_tpatterns
