# Python I2C Driver for Sensirion SFM-SF06

This repository contains the Python driver to communicate with a Sensirion sensor of the SFM-SF06 family over I2C.

<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sfm_sf06/master/images/SFM4300.png"
    width="300px" alt="SFM-SF06 picture">


Click [here](https://sensirion.com/products/product-categories/gas-flow-sensors/) to learn more about the Sensirion SFM-SF06 sensor family.


Not all sensors of this driver family support all measurements.
In case a measurement is not supported by all sensors, the products that
support it are listed in the API description.



## Supported sensor types

| Sensor name   | I²C Addresses  |
| ------------- | -------------- |
|[SFM4300](https://sensirion.com/products/catalog/?filter_series=77ed9322-c043-4eaf-ad3c-2b55aae69cdd)| **0x2a**, 0x2b, 0x2c, 0x2d|
|[SFM3119](https://sensirion.com/products/catalog/SFM3119/)| **0x29**|
|[SFM3003](https://sensirion.com/products/catalog/SEK-SFM3003/)| **0x28**, 0x2d|
|[SFM3013](https://sensirion.com/products/catalog/SEK-SFM3013/)| **0x2f**|
|[SFM3019](https://sensirion.com/products/catalog/SEK-SFM3019/)| **0x2e**|

The following instructions and examples use a *SFM4300*.



## Connect the sensor

You can connect your sensor over a [SEK-SensorBridge](https://developer.sensirion.com/product-support/sek-sensorbridge/).
For special setups you find the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-sfm_sf06/master/images/pinout_SFM4300.png"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 |  | ADDR |  | see data sheet section 4.1
| 2 |  | SDA | I2C: Serial data input / output | Serial data, bidirectional
| 3 |  | GND | Ground |
| 4 |  | VDD | Supply Voltage | 3.0V to 5.0V
| 5 |  | SCL | I2C: Serial clock input |
| 6 |  | IRQn |  | Active low. see data sheet section 3.3


</p>
</details>


## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-i2c-sfm_sf06) for an API description and a
[quickstart](https://sensirion.github.io/python-i2c-sfm_sf06/quickstart.html) example.


## Contributing

In case you want to contribute to this project, please read the [contribution guidelines]((https://sensirion.github.io/python-i2c-sfm_sf06/contributing.html)).

## License

See [LICENSE](LICENSE).