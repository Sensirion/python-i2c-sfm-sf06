#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland
import time

import pytest

from sensirion_i2c_sfm_sf06.response_types import Flow, Temperature


@pytest.mark.needs_device
def test_enter_sleep(device):
    """
    Test if the device is not responsive after entering sleep
    """
    device.enter_sleep()
    device_sleeping = False
    try:
        product_id, serial_number = device.read_product_identifier()
    except Exception:
        device_sleeping = True
    assert device_sleeping


@pytest.mark.needs_device
def test_enter_exit_sleep(device):
    """
    Test if the device is not responsive after entering sleep
    """
    device.enter_sleep()
    time.sleep(0.5)
    device.exit_sleep()
    time.sleep(0.5)
    test_get_product_identifier(device)


@pytest.mark.needs_device
def test_get_product_identifier(device):
    """
    Get serial number and verify it is valid (non-zero)
    """
    product_id, serial_number = device.read_product_identifier()
    assert type(product_id) is int
    assert type(serial_number) is bytes
    assert product_id != 0
    assert serial_number != 0, "serial number can't be zero"


@pytest.mark.needs_device
def test_configure_averaging(device):
    device.configure_averaging(0)


@pytest.mark.needs_device
def test_update_concentration(device):
    try:
        device.start_Air_O2_continuous_measurement(50)
        for i in range(3):
            _ = device.read_measurement_data()
        device.update_concentration(25)
        for i in range(3):
            _ = device.read_measurement_data()
    finally:
        device.stop_continuous_measurement()


@pytest.mark.needs_device
def test_one_gas_measure(device):
    """
    Perform a measurement
    """
    measurement_functions = [device.start_O2_continuous_measurement,
                             device.start_air_continuous_measurement,
                             device.start_N2O_continuous_measurement,
                             device.start_CO2_continuous_measurement,
                             lambda: device.start_Air_O2_continuous_measurement(50),
                             lambda: device.start_CO2_O2_continuous_measurement(50),
                             lambda: device.start_N2O_O2_continuous_measurement(50)]
    for start_measure in measurement_functions:
        start_measure()
        try:
            for i in range(3):
                result = device.read_measurement_data()
                assert isinstance(result, tuple)
                assert len(result) == 3
                assert isinstance(result[0], Flow)
                assert isinstance(result[1], Temperature)
                print("flow:", result[0])
                print("temperature:", result[1])
                print("status word:", result[2])
        finally:
            device.stop_continuous_measurement()
