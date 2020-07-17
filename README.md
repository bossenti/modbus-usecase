# Modbus UseCase

This repository's code is used to simulate a pump.
Modbus is used to access the sensor data, query and transport it over the network.
We use this for a tutorial for Apache StreamPipes, see the corresponding [blog post]().

<br>
To provide this functionality we need two simple scripts:

 - `modbus_device.py`: This script provides a Modbus device as a little server. It's based on the library `pymodbus` and uses one of their [code examples](https://pymodbus.readthedocs.io/en/latest/source/example/synchronous_server.html).
 - `modbus_data_insert.py`: It's only function is to write values from the provided csv row-wise to the `HoldingRegister` of the Modbus device.
 
 <br>
 The data set we use here, is just a short record of pump of which we use the following sensor data:  

- density
- fluid temperature
- mass flow
- sensor fault flags
- volume flow
