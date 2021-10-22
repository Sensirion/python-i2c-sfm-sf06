#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_i2c_sfm_sf06.response_types import Flow, Temperature

import pytest


@pytest.mark.parametrize("value", [
    dict({'measurement': 5000}),
    dict({'measurement': 4500}),
])
def test_temperature_signal(value):
    """
    Test if mass concentration is scaled properly.

    All value wrappers in this module derive from the same base class and do not include any code
    but the class definition.
    Therefore only on value wrapper is tested.
    """
    result = Temperature(value.get('measurement'))
    assert type(result) is Temperature
    assert type(result.value) is float
    assert result.value == value.get('measurement') / 200  # temperature scaling is 200


@pytest.mark.parametrize("value", [
    dict({'measurement': 205, 'scaling': 10, 'offset': 5}),
    dict({'measurement': 1000, 'scaling': 3, 'offset': -500}),
    dict({'measurement': 405, 'scaling': 5, 'offset': 200}),
])
def test_flow_signal(value):
    """
    Test if values are scaled according specified scaling
    """
    result = Flow(value.get('measurement'), scaling=value.get('scaling'), offset=value.get('offset'))
    assert type(result) is Flow
    assert type(result.value) is float
    assert result.value == (value.get('measurement')-value.get('offset')) / value.get('scaling')
