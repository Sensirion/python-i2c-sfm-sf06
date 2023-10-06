#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from .version import version as __version__  # noqa: F401

from sensirion_i2c_sfm_sf06.device import SfmSf06Device  # noqa: F401

__all__ = ['SfmSf06Device']
