Quick Start
===========

SensorBridge Example
--------------------

Following example code shows how to use this driver with a Sensirion SFM-SF06
connected to the computer using a `Sensirion SEK-SensorBridge`_. The driver
for the SensorBridge can be installed with

.. sourcecode:: bash

    pip install sensirion-shdlc-sensorbridge

.. _Sensirion SEK-SensorBridge: https://www.sensirion.com/sensorbridge/

SFM SF06
--------

.. sourcecode:: python

    import time
    from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
    from sensirion_shdlc_sensorbridge import SensorBridgePort, \
        SensorBridgeShdlcDevice, SensorBridgeI2cProxy
    from sensirion_i2c_driver import I2cConnection
    from sensirion_i2c_sfm_sf06 import SFM_SF06Driver

    # Connect to the SensorBridge with default settings:
    #  - baudrate:      460800
    #  - slave address: 0
    with ShdlcSerialPort(port='COM1', baudrate=460800) as port:
        #TBD


Linux I²C Hardware
------------------

The following examples show how to use the SFM SF06 sensor with a generic Linux I²C hardware
(e.g. attached to the Raspberry Pi I²C port 1)


.. sourcecode:: python

    import time
    from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection
    #TBD
