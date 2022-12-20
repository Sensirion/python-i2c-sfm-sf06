#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland
import time

import pytest

from sensirion_i2c_sfm_sf06.result_types import SignalFlow, SignalTemperature


@pytest.mark.needs_device
def test_enter_sleep(sensor):
    """
    Test if the sensor is not responsive after entering sleep
    """
    sensor.enter_sleep()
    device_sleeping = False
    try:
        product_id, serial_number = sensor.read_product_identifier()
    except Exception:
        device_sleeping = True
    assert device_sleeping


@pytest.mark.needs_device
def test_enter_exit_sleep(sensor):
    """
    Test if the sensor is not responsive after entering sleep
    """
    sensor.enter_sleep()
    time.sleep(0.5)
    sensor.exit_sleep()
    time.sleep(0.5)
    test_get_product_identifier(sensor)


@pytest.mark.needs_device
def test_get_product_identifier(sensor):
    """
    Get serial number and verify it is valid (non-zero)
    """
    product_id, serial_number = sensor.read_product_identifier()
    assert isinstance(product_id, int)
    assert isinstance(serial_number, int)
    assert product_id != 0
    assert serial_number != 0


@pytest.mark.needs_device
def test_configure_averaging(sensor):
    sensor.configure_averaging(0)


@pytest.mark.needs_device
def test_update_concentration(sensor):
    try:
        sensor.start_air_o2_continuous_measurement(50)
        for i in range(3):
            _ = sensor.read_measurement_data()
        sensor.update_concentration(25)
        for i in range(3):
            _ = sensor.read_measurement_data()
    finally:
        sensor.stop_continuous_measurement()


@pytest.mark.needs_device
def test_one_gas_measure(sensor):
    """
    Perform a measurement
    """
    measurement_functions = [sensor.start_o2_continuous_measurement,
                             sensor.start_air_continuous_measurement,
                             sensor.start_n2o_continuous_measurement,
                             sensor.start_co2_continuous_measurement,
                             lambda: sensor.start_air_o2_continuous_measurement(50),
                             lambda: sensor.start_co2_o2_continuous_measurement(50),
                             lambda: sensor.start_n2o_o2_continuous_measurement(50)]
    for start_measure in measurement_functions:
        start_measure()
        try:
            for i in range(3):
                result = sensor.read_measurement_data()
                assert isinstance(result, tuple)
                assert len(result) == 3
                assert isinstance(result[0], SignalFlow)
                assert isinstance(result[1], SignalTemperature)
                print("flow:", result[0])
                print("temperature:", result[1])
                print("status word:", result[2])
        finally:
            sensor.stop_continuous_measurement()
