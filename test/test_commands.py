#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function

import pytest


@pytest.mark.needs_device
def test_get_product_identifier(device):
    """
    Get serial number and verify it is valid (non-zero)
    """
    product_id, serial_number = device.read_product_identifier()
    assert type(product_id) is int
    assert type(serial_number) is int
    assert product_id != 0
    assert serial_number != 0, "serial number can't be zero"


@pytest.mark.needs_device
def test_measure(device):
    """
    Perform a measurement
    """
    device.start_O2_continuous_measurement()
    try:
        for i in range(3):
            result = device.read_measurement_data()
            assert isinstance(result, tuple)
            assert len(result) == 3
            print("flow:", result[0])
            print("temperature:", result[1])
            print("status word:", result[2])

    finally:
        device.stop_continuous_measurement()
