#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2023 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:    sensirion-driver-generator 0.20.0
# Product:      sfm_sf06
# Version:      1.0
#
"""
The transfer classes specify the data that is transferred between host and sensor. The generated transfer classes
are used by the driver class and not intended for direct use.
"""

from enum import Enum
from sensirion_driver_adapters.transfer import Transfer
from sensirion_driver_adapters.rx_tx_data import TxData, RxData
from sensirion_driver_support_types.bitfield import BitField, BitfieldContainer


class ErrorCodeT(Enum):
    I2C_ERROR = 0
    TIMEOUT = 1

    def __int__(self):
        return self.value


class StatusWordT(BitfieldContainer):
    command_code = BitField(offset=12, width=4)
    exp_smoothing_flag = BitField(offset=11, width=1)
    avg_mode_flag = BitField(offset=10, width=1)
    gas_conc = BitField(offset=0, width=10)


class FlowUnitT(BitfieldContainer):
    prefix = BitField(offset=0, width=3)
    time_base = BitField(offset=4, width=4)
    unit = BitField(offset=8, width=4)


class StartO2ContinuousMeasurement(Transfer):
    """
    The sensor starts measuring both O₂ flow and temperature and provides a status word. All three measurement results can
    be read out through one single I2C read when the continuous measurement is running. The specific command code used for the
    start continuous measurement command selects the calibrated gas or binary gas mixture (lookup table) for the flow signal.

    Supported by products:
      - SFM3003
      - SFM4300
      - SFM3119
      - SFM3013
      - SFM3019
    """

    CMD_ID = 0x3603

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.012, slave_address=None, ignore_ack=False)


class StartAirContinuousMeasurement(Transfer):
    """
    The sensor starts measuring both Air flow and temperature and provides a status word. All three measurement results can
    be read out through one single I2C read when the continuous measurement is running. The specific command code used for the
    start continuous measurement command selects the calibrated gas or binary gas mixture (lookup table) for the flow signal.

    Supported by products:
      - SFM3003
      - SFM4300
      - SFM3119
      - SFM3013
      - SFM3019
    """

    CMD_ID = 0x3608

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H')


class StartN2OContinuousMeasurement(Transfer):
    """
    The sensor starts measuring both N₂O (*HeOx for SMF3012*) flow and temperature and provides a status word. All three measurement results
    can be read out through one single I2C read when the continuous measurement is running. The specific command code used
    for the start continuous measurement command selects the calibrated gas or binary gas mixture (lookup table) for the flow
    signal.

    Supported by products:
      - SFM4300
      - SFM3013 (HeOx)
    """

    CMD_ID = 0x3615

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.012, slave_address=None, ignore_ack=False)


class StartCO2ContinuousMeasurement(Transfer):
    """
    The sensor starts measuring both CO₂ flow and temperature and provides a status word. All three measurement results
    can be read out through one single I2C read when the continuous measurement is running.
    The specific command code used for the start continuous measurement command selects the calibrated gas or binary
    gas mixture (lookup table) for the flow signal.

    Supported by products:
      - SFM4300
    """

    CMD_ID = 0x361e

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.012, slave_address=None, ignore_ack=False)


class StartAirO2ContinuousMeasurement(Transfer):
    """
    The sensor starts measuring the Air/O₂ flow and temperature and provides a status word. All three measurement results
    can be read out through one single I2C read when the continuous measurement is running.
    The specific command code used for the start continuous measurement command selects the calibrated gas or binary
    gas mixture (lookup table) for the flow signal.

    Supported by products:
      - SFM3003
      - SFM4300
      - SFM3119
      - SFM3013
      - SFM3019
    """

    CMD_ID = 0x3632

    def __init__(self, volume_fraction):
        self._volume_fraction = volume_fraction

    def pack(self):
        return self.tx_data.pack([self._volume_fraction])

    tx = TxData(CMD_ID, '>HH', device_busy_delay=0.012, slave_address=None, ignore_ack=False)


class StartN2OO2ContinuousMeasurement(Transfer):
    """
    The sensor starts measuring the  N₂O / O₂ flow and temperature and provides a status word. All three measurement results
    can be read out through one single I2C read when the continuous measurement is running.
    The specific command code used for the start continuous measurement command selects the calibrated gas or binary
    gas mixture (lookup table) for the flow signal.

    Supported by products:
      - SFM4300
      - SFM3013 (HeOx)
    """

    CMD_ID = 0x3639

    def __init__(self, volume_fraction):
        self._volume_fraction = volume_fraction

    def pack(self):
        return self.tx_data.pack([self._volume_fraction])

    tx = TxData(CMD_ID, '>HH', device_busy_delay=0.012, slave_address=None, ignore_ack=False)


class StartCO2O2ContinuousMeasurement(Transfer):
    """
    The sensor starts measuring the  CO₂ / O₂ flow and temperature and provides a status word. All three measurement results
    can be read out through one single I2C read when the continuous measurement is running.
    The specific command code used for the start continuous measurement command selects the calibrated gas or binary
    gas mixture (lookup table) for the flow signal.

    Supported by products:
      - SFM4300
    """

    CMD_ID = 0x3646

    def __init__(self, volume_fraction):
        self._volume_fraction = volume_fraction

    def pack(self):
        return self.tx_data.pack([self._volume_fraction])

    tx = TxData(CMD_ID, '>HH', device_busy_delay=0.012, slave_address=None, ignore_ack=False)


class ReadMeasurementData(Transfer):
    """
    After the command *start_xx_continuous_measurement* has been sent, the chip continuously measures and updates the
    measurement results.
    New results (flow, temperature, and status word) can be read continuously with this command.
    """

    def pack(self):
        return None

    rx = RxData('>hhH')


class UpdateConcentrationSet(Transfer):
    """
    Together with the instruction *update_concentration_activate* this instruction allows to update the concentration
    of a binary gas mixture dynamically, i.e. without exiting the running measurement mode.
    This first instruction transmits the new concentration value to the flow sensor.
    This instruction refers to *Transmit concentration*. For more details see data-sheet section *Update Concentration*
    """

    CMD_ID = 0xe17d

    def __init__(self, volume_fraction):
        self._volume_fraction = volume_fraction

    def pack(self):
        return self.tx_data.pack([self._volume_fraction])

    tx = TxData(CMD_ID, '>HH')


class UpdateConcentrationActivate(Transfer):
    """
    By executing this instruction the previously with *update_concentration_set* set value becomes active.
    The instruction resets the I2C address pointer to the regular result output buffer such that the measurement
    data as described by the transfer read_measurement_data are optained upon a subsequent read.
    This instruction refers to *Reset-i2c address pointer*. For more details see data-sheet section *Update Concentration*
    """

    CMD_ID = 0xe000

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H')


class StopContinuousMeasurement(Transfer):
    """
    This command stops the continuous measurement and puts
    the sensor in idle mode. After it receives the stop command,
    the sensor needs up to 0.5ms to power down the heater, enter
    idle mode and be receptive for a new command.
    """

    CMD_ID = 0x3ff9

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H')


class ConfigureAveraging(Transfer):
    """
    This command configures the sensor’s averaging mode:
      - N=0 (default): average-until-read mode (c.f. Sec. 3)
      - 1≤N≤128: fixed-N averaging mode. N is the number of internal
        measurements that are averaged for one returned
        measurement value (i.e. the average over N flow samples,
        where N = CmdArgument, c.f. Sec. 3).

    The configured averaging mode will be used for flow measurements
    until a reset or re-execution of this command is performed. After a
    reset, averaging is set to average-until-read mode (i.e. N is set to 0).
    The highest averaging number allowed is 128. If a higher number is
    used in the command argument, it will be overruled by the maximal
    value of 128 samples to average.
    If no averaging is desired, set N to 1.
    """

    CMD_ID = 0x366a

    def __init__(self, average_window):
        self._average_window = average_window

    def pack(self):
        return self.tx_data.pack([self._average_window])

    tx = TxData(CMD_ID, '>HH')


class ReadScaleOffsetUnit(Transfer):
    """
    This command provides the scale factor and offset to convert flow readings into physical units. The scale factor
    and offset are specific to the calibrated gas / gas mixture and its corresponding lookup table used for the
    flow measurement. Therefore, the gas / gas mixture needs to be specified in the command argument by the command code
    of the corresponding start continuous measurement. For detailed information see data-sheet.
    """

    CMD_ID = 0x3661

    def __init__(self, command_code):
        self._command_code = command_code

    def pack(self):
        return self.tx_data.pack([self._command_code])

    tx = TxData(CMD_ID, '>HH')
    rx = RxData('>hhH')


class EnterSleep(Transfer):
    """
    In sleep mode the sensor uses a minimum amount of power. The mode can only be entered from idle mode, i.e. when the
    sensor is not performing measurements.
    This mode is particularly useful for battery operated devices. To minimize the current in this mode, the complexity of the sleep
    mode circuit has been reduced as much as possible, which is mainly reflected by the way the sensor exits the sleep mode. In
    sleep mode the sensor cannot be soft reset.
    """

    CMD_ID = 0x3677

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H', device_busy_delay=0.0, slave_address=None, ignore_ack=True)


class ExitSleep(Transfer):
    """
    The sensor exits the sleep mode and enters the idle mode when
    it receives the valid I2C address and a write bit (‘0’).
    Note that the I2C address is not acknowledged. It is necessary to
    poll the sensor to see whether the sensor has received the
    address and has woken up. This should take typically 16ms.
    """

    CMD_ID = 0x0

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>B', device_busy_delay=0.0, slave_address=None, ignore_ack=True)


class ReadProductIdentifier(Transfer):
    """
    This command allows to read product identifier and the serial number.
    The command can only be executed from the idle mode, i.e. when the sensor is not performing measurements
    """

    CMD_ID = 0xe102

    def pack(self):
        return self.tx_data.pack([])

    tx = TxData(CMD_ID, '>H')
    rx = RxData(descriptor='>I8B', convert_to_int=True)
