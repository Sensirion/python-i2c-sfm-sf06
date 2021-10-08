#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function


class Temperature(object):
    """
    Represents a temperature measurement value

    :param int scaled temperature value:
        The read value as it is returned from the sensor.
    """

    def __init__(self, value):
        """
        Creates an instance from the received raw data.
        """
        #: The converted sensor value (raw sensor value divided by scaling)
        self._value = value / 200.0

    @property
    def value(self):
        return self._value

    def __str__(self):
        return '{:.2f}'.format(self.value)


class Flow(object):
    """
    Represents a flow measurement value

    :param int scaled flow value:
        The read value as it is returned from the sensor.
    """

    def __init__(self, value, scale=1, offset=0):
        """
        Creates an instance from the received raw data.
        """
        #: The converted sensor value (raw sensor value divided by scaling)
        self._value = (value - offset) / scale

    @property
    def value(self):
        return self._value

    def __str__(self):
        return '{:.2f}'.format(self.value)
