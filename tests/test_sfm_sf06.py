#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2024 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:     sensirion-driver-generator 0.37.0
# Product:       sfm_sf06
# Model-Version: 1.5.0
#

import pytest
from sensirion_i2c_sfm_sf06.device import SfmSf06Device


@pytest.fixture
def sensor(channel_provider):
    channel_provider.i2c_frequency = 100e3
    channel_provider.supply_voltage = 3.3
    with channel_provider:
        channel = channel_provider.get_channel(slave_address=0x2A,
                                               crc_parameters=(8, 0x31, 0xff, 0x0))
        yield SfmSf06Device(channel)


def test_configure_averaging1(sensor):
    sensor.configure_averaging(50)


def test_read_product_identifier1(sensor):
    (product_identifier, serial_number
     ) = sensor.read_product_identifier()
    print(f"product_identifier: {product_identifier}; "
          f"serial_number: {serial_number}; "
          )


def test_enter_sleep1(sensor):
    sensor.enter_sleep()
    sensor.exit_sleep()


def test_start_O2_continuous_measurement1(sensor):
    sensor.start_o2_continuous_measurement()
    (a_flow, a_temperature, a_status_word
     ) = sensor.read_measurement_data()
    print(f"a_flow: {a_flow}; "
          f"a_temperature: {a_temperature}; "
          f"a_status_word: {a_status_word}; "
          )
    sensor.stop_continuous_measurement()


def test_start_Air_continuous_measurement1(sensor):
    sensor.start_air_continuous_measurement()
    (a_flow, a_temperature, a_status_word
     ) = sensor.read_measurement_data()
    print(f"a_flow: {a_flow}; "
          f"a_temperature: {a_temperature}; "
          f"a_status_word: {a_status_word}; "
          )
    sensor.stop_continuous_measurement()


def test_start_N2O_continuous_measurement1(sensor):
    sensor.start_n2o_continuous_measurement()
    (a_flow, a_temperature, a_status_word
     ) = sensor.read_measurement_data()
    print(f"a_flow: {a_flow}; "
          f"a_temperature: {a_temperature}; "
          f"a_status_word: {a_status_word}; "
          )
    sensor.stop_continuous_measurement()


def test_start_CO2_continuous_measurement1(sensor):
    sensor.start_co2_continuous_measurement()
    (a_flow, a_temperature, a_status_word
     ) = sensor.read_measurement_data()
    print(f"a_flow: {a_flow}; "
          f"a_temperature: {a_temperature}; "
          f"a_status_word: {a_status_word}; "
          )
    sensor.stop_continuous_measurement()


def test_start_N2O_O2_continuous_measurement1(sensor):
    sensor.start_n2o_o2_continuous_measurement(50)
    (a_flow, a_temperature, a_status_word
     ) = sensor.read_measurement_data()
    print(f"a_flow: {a_flow}; "
          f"a_temperature: {a_temperature}; "
          f"a_status_word: {a_status_word}; "
          )
    sensor.update_concentration(50)
    sensor.stop_continuous_measurement()


def test_start_Air_O2_continuous_measurement1(sensor):
    sensor.start_air_o2_continuous_measurement(50)
    (a_flow, a_temperature, a_status_word
     ) = sensor.read_measurement_data()
    print(f"a_flow: {a_flow}; "
          f"a_temperature: {a_temperature}; "
          f"a_status_word: {a_status_word}; "
          )
    sensor.update_concentration(50)
    sensor.stop_continuous_measurement()


def test_start_CO2_O2_continuous_measurement1(sensor):
    sensor.start_co2_o2_continuous_measurement(50)
    (a_flow, a_temperature, a_status_word
     ) = sensor.read_measurement_data()
    print(f"a_flow: {a_flow}; "
          f"a_temperature: {a_temperature}; "
          f"a_status_word: {a_status_word}; "
          )
    sensor.update_concentration(50)
    sensor.stop_continuous_measurement()

