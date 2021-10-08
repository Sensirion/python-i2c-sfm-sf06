# -*- coding: utf-8 -*-
#
# (c) Copyright 2021 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:    sensirion-driver-generator 0.1.0
# Product:      SFM_SF06
# Version:      1.0
#

from sensirion_i2c_adapter.transfer import execute_transfer

from commands import *
from sensirion_i2c_sfm_sf06.response_types import Flow, Temperature


class SfmSf06Device:

    def __init__(self, channel):
        self._channel = channel
        self._scale = 1
        self._offset = 0
        self._flow_unit = 0

    def start_O2_continuous_measurement(self):
        """
        The sensor starts measuring both O₂ flow and temperature and provides a status word. All three measurement
        results can be read out through one single I2C read when the continuous measurement is running.
        The specific command code used for the start continuous measurement command selects the calibrated gas or
        binary gas mixture (lookup table) for the flow signal.
        Supported by products:
          - SFM3003
          - SFM4300
          - SFM3119
          - SFM3012
          - SFM3019
        """
        transfer = StartO2ContinuousMeasurement()
        return execute_transfer(self._channel, transfer)

    def start_air_continuous_measurement(self):
        """
        The sensor starts measuring both Air flow and temperature and provides a status word. All three measurement
        results can be read out through one single I2C read when the continuous measurement is running.
        The specific command code used for the start continuous measurement command selects the calibrated gas or
        binary gas mixture (lookup table) for the flow signal.
        Supported by products:
          - SFM3003
          - SFM4300
          - SFM3119
          - SFM3012
          - SFM3019
        """
        transfer = StartAirContinuousMeasurement()
        return execute_transfer(self._channel, transfer)

    def start_N2O_continuous_measurement(self):
        """
        The sensor starts measuring both N₂O (*HeOx for SMF3012*) flow and temperature and provides a status word.
        All three measurement results can be read out through one single I2C read when the continuous measurement is
        running. The specific command code used for the start continuous measurement command selects the calibrated
        gas or binary gas mixture (lookup table) for the flow signal.
        Supported by products:
          - SFM4300
          - SFM3013 (HeOx)
        """
        transfer = StartN2OContinuousMeasurement()
        return execute_transfer(self._channel, transfer)

    def start_CO2_continuous_measurement(self):
        """
        The sensor starts measuring both CO₂ flow and temperature and provides a status word. All three measurement
        results can be read out through one single I2C read when the continuous measurement is running.
        The specific command code used for the start continuous measurement command selects the calibrated gas or binary
        gas mixture (lookup table) for the flow signal.
        Supported by products:
          - SFM4300
        """
        transfer = StartCO2ContinuousMeasurement()
        return execute_transfer(self._channel, transfer)

    def start_Air_O2_continuous_measurement(self, volume_fraction):
        """
        The sensor starts measuring the Air/O₂ flow and temperature and provides a status word. All three measurement
        results can be read out through one single I2C read when the continuous measurement is running.
        The specific command code used for the start continuous measurement command selects the calibrated gas or binary
        gas mixture (lookup table) for the flow signal.
        Supported by products:
          - SFM3003
          - SFM4300
          - SFM3119
          - SFM3012
          - SFM3019
        
        :param volume_fraction:
            Volume fraction of dioxigen in ‰.
        """
        transfer = StartAirO2ContinuousMeasurement(volume_fraction)
        return execute_transfer(self._channel, transfer)

    def start_NO2_O2_continuous_measurement(self, volume_fraction):
        """
        The sensor starts measuring the  N₂O / O₂ flow and temperature and provides a status word. All three
        measurement results can be read out through one single I2C read when the continuous measurement is running.
        The specific command code used for the start continuous measurement command selects the calibrated gas or binary
        gas mixture (lookup table) for the flow signal.
        Supported by products:
          - SFM4300
          - SFM3013 (HeOx)
        
        :param volume_fraction:
            Volume fraction of O₂ in ‰.
        """
        transfer = StartNO2O2ContinuousMeasurement(volume_fraction)
        return execute_transfer(self._channel, transfer)

    def start_C02_02_continuous_measurement(self, volume_fraction):
        """
        The sensor starts measuring the  CO₂ / O₂ flow and temperature and provides a status word.
        All three measurement results can be read out through one single I2C read when the continuous measurement is
        running.
        The specific command code used for the start continuous measurement command selects the calibrated gas or binary
        gas mixture (lookup table) for the flow signal.
        Supported by products:
          - SFM4300
        
        :param volume_fraction:
            Volume fraction of O₂ in ‰.
        """
        transfer = StartC0202ContinuousMeasurement(volume_fraction)
        return execute_transfer(self._channel, transfer)

    def read_measurement_data(self):
        """
        After the command *start_xx_continuous_measurement* has been sent, the chip continuously measures and updates
        the measurement results.
        New results (flow, temperature, and status word) can be read continuously with this command.
        :return flow:
            Read calibrated flow signal read from the sensor.
        :return temperature:
            Temperature scaled with a factor of 200.
        :return status_word:
            Gives information about the measurement command that is currently running, information on the currently
            selected averaging mode, and the defined gas concentration of the current measurement command.
            A detailed description of the *status_word* can be found in the data sheet.
        """
        transfer = ReadMeasurementData()
        flow, temperature, status_word = execute_transfer(self._channel, transfer)
        return Flow(flow, scale=self._scale, offset=self._offset), Temperature(temperature), status_word

    def update_concentration_set(self, volume_fraction):
        """
        Together with the instruction *update_concentration_activate* this instruction allows to update the
        concentration of a binary gas mixture dynamically, i.e. without exiting the running measurement mode.
        This first instruction transmits the new concentration value to the flow sensor.
        This instruction refers to *Transmit concentration*. For more details see data-sheet section
        *Update Concentration*
        
        :param volume_fraction:
            New O₂ volume fraction
        """
        transfer = UpdateConcentrationSet(volume_fraction)
        return execute_transfer(self._channel, transfer)

    def update_concentration_activate(self):
        """
        By executing this instruction the previously with *update_concentration_set* set value becomes active.
        The instruction resets the I2C address pointer to the regular result output buffer such that the measurement
        data as described by the transfer read_measurement_data are optained upon a subsequent read.
        This instruction refers to *Reset-i2c address pointer*. For more details see data-sheet section
        *Update Concentration*
        """
        transfer = UpdateConcentrationActivate()
        return execute_transfer(self._channel, transfer)

    def update_concentration(self, volume_fraction):
        """
        Sets and aktivates a new volume fraction of a binary gas mixtures

        :param volume_fraction:
            New O₂ volume fraction 
        """
        self.update_concentration_set(volume_fraction)
        return self.update_concentration_activate()

    def stop_continuous_measurement(self):
        """
        This command stops the continuous measurement and puts
        the sensor in idle mode. After it receives the stop command,
        the sensor needs up to 0.5ms to power down the heater, enter
        idle mode and be receptive for a new command.
        """
        transfer = StopContinuousMeasurement()
        return execute_transfer(self._channel, transfer)

    def configure_averaging(self, average_window):
        """
        This command configures the sensor’s averaging mode:
        1) N=0 (default): average-until-read mode (c.f. Sec. 3)
        2) 1≤N≤128: fixed-N averaging mode. N is the number of internal
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
        
        :param average_window:
            Average window configuration value.
        """
        transfer = ConfigureAveraging(average_window)
        return execute_transfer(self._channel, transfer)

    def read_scale_offset_flow(self):
        """
        This command provides the scale factor and offset to convert flow readings into physical units. The scale factor
        and offset are specific to the calibrated gas / gas mixture and its corresponding lookup table used for the
        flow measurement. Therefore, the gas / gas mixture needs to be specified in the command argument by the command
        code of the corresponding start continuous measurement. For detailed information see data-sheet.
        :return scale_factor:
            Scale factor used by the sensor.
        :return offset:
            Offset used by the sensor.
        :return flow_unit:
            Applicable flow unit.
        """
        transfer = ReadScaleOffsetFlow()
        self._scale, self._offset, self._flow_unit = execute_transfer(self._channel, transfer)
        return self._scale, self._offset, self._flow_unit

    def enter_sleep(self):
        """
        In sleep mode the sensor uses a minimum amount of power. The mode can only be entered from idle mode, i.e.
        when the sensor is not performing measurements.
        This mode is particularly useful for battery operated devices. To minimize the current in this mode, the
        complexity of the sleep mode circuit has been reduced as much as possible, which is mainly reflected by the
        way the sensor exits the sleep mode. In sleep mode the sensor cannot be soft reset.
        """
        transfer = EnterSleep()
        return execute_transfer(self._channel, transfer)

    def exit_sleep(self):
        """
        The sensor exits the sleep mode and enters the idle mode when
        it receives the valid I2C address and a write bit (‘0’).
        Note that the I2C address is not acknowledged. It is necessary to
        poll the sensor to see whether the sensor has received the
        address and has woken up. This should take typically 16ms.
        """
        transfer = ExitSleep()
        return execute_transfer(self._channel, transfer)

    def read_product_identifier(self):
        """
        This command allows to read product identifier and the serial number.
        The command can only be executed from the idle mode, i.e. when the sensor is not performing measurements
        :return product_identifier:
            32-bit unique product and revision number
        :return serial_number:
            64 bit unique serial number of the device
        """
        transfer = ReadProductIdentifier()
        return execute_transfer(self._channel, transfer)