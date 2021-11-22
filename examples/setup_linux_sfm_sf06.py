from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection, CrcCalculator

from sensirion_i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_sfm_sf06.device import SfmSf06Device

# Connect to the I²C 1 port /dev/i2c-1
with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
    # Create channel

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
