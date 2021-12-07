Quick Start
===========

SensorBridge Example
--------------------

The following example code shows how to use this SFM-SF06 driver with a
Sensirion SFM4300 sensor connected to the computer using a
`Sensirion SEK-SensorBridge`_. The driver for the SensorBridge can be installed with

.. sourcecode:: bash

    pip install sensirion-shdlc-sensorbridge

.. _Sensirion SEK-SensorBridge: https://www.sensirion.com/sensorbridge/

SFM-SF06
--------

.. sourcecode:: python

.. literalinclude:: ../examples/setup_sensorbridge_sfm_sf06.py

Linux I²C Hardware
------------------

The following example shows how to use the SFM-SF06 driver with a generic Linux I²C hardware
(e.g. attached to the Raspberry Pi I²C port 1)


.. sourcecode:: python

.. literalinclude:: ../examples/setup_linux_sfm_sf06.py
