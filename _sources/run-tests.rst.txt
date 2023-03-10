Run tests
=========

Unit tests can be run with `pytest <https://pytest.org>`_:

.. code-block:: bash

    pip install -e .[test]                       # Install requirements
    pytest -m "not needs_device"                 # Run tests without hardware
    pytest                                       # Run all tests
    pytest -m "needs_device"                     # Run all tests for SFM-SF06


The tests with the marker `needs_device` have following requirements:

- The SFM-SF06 sensor must be connected to a
  `SensorBridge <https://sensirion.com/products/catalog/SEK-SensorBridge/>`_ on port 1.
- Pass the serial port where the SensorBridge is connected with
  `--serial-port`, e.g. `pytest --serial-port=COM7`
- The SensorBridge must have default settings (baudrate 460800, address 0)

