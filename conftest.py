# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function

import pytest
from sensirion_i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_driver import I2cConnection, CrcCalculator
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import SensorBridgePort, \
    SensorBridgeShdlcDevice, SensorBridgeI2cProxy

from sensirion_i2c_sfm_sf06.device import SfmSf06Device


def pytest_addoption(parser):
    """
    Register command line options
    """
    parser.addoption("--serial-port", action="store", type=str)
    parser.addoption("--serial-bitrate", action="store", type=int, default=460800)


def _get_serial_port(config, validate=False):
    """
    Get the serial port to be used for the tests.
    """
    port = config.getoption("--serial-port")
    if (validate is True) and (port is None):
        raise ValueError("Please specify the serial port to be used with "
                         "the '--serial-port' argument.")
    return port


def _get_serial_bitrate(config):
    """
    Get the serial port bitrate to be used for the tests.
    """
    return config.getoption("--serial-bitrate")


def pytest_report_header(config):
    """
    Add extra information to test report header
    """
    lines = [
        "SensorBridge serial port: " + str(_get_serial_port(config)),
        "SensorBridge serial bitrate: " + str(_get_serial_bitrate(config))
    ]
    return '\n'.join(lines)


@pytest.fixture(scope="session")
def bridge(request):
    serial_port = _get_serial_port(request.config, validate=True)
    serial_bitrate = _get_serial_bitrate(request.config)
    with ShdlcSerialPort(serial_port, serial_bitrate) as port:
        dev = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
        yield dev


@pytest.fixture
def device(bridge):
    # Configure SensorBridge port 1 for SFM-SF06
    bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
    bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=5.0)
    bridge.switch_supply_on(SensorBridgePort.ONE)

    # Create SFM-SF06 device
    i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
    channel = I2cChannel(I2cConnection(i2c_transceiver),
                         slave_address=0x29,
                         crc=CrcCalculator(8, 0x31, 0xFF, 0x00))
    dev = SfmSf06Device(channel)

    yield dev

    # make sure the channel is powered off after executing tests
    bridge.switch_supply_off(SensorBridgePort.ONE)
