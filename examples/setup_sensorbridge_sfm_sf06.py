from sensirion_i2c_driver import I2cConnection, CrcCalculator
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import SensorBridgePort, \
    SensorBridgeShdlcDevice, SensorBridgeI2cProxy

from sensirion_i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_sfm_sf06.device import SfmSf06Device

# for linux
with ShdlcSerialPort(port='COM1', baudrate=460800) as port:
    bridge = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
    bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
    bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=5.0)
    bridge.switch_supply_on(SensorBridgePort.ONE)

    # Create the channel
    i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
    channel = I2cChannel(I2cConnection(i2c_transceiver),
                         slave_address=0x2A,  # this is the configuration of sfm4300
                         crc=CrcCalculator(8, 0x31, 0xFF, 0x00))
    # create the sensor
    sfm_sensor = SfmSf06Device(channel)

    # start measuring
    sfm_sensor.start_O2_continuous_measurement()
    try:

        for i in range(10):
            flow, temperature, status = sfm_sensor.read_measurement_data()
            print('flow:', flow)
            print('temperature:', temperature)
    finally:
        sfm_sensor.stop_continuous_measurement()
