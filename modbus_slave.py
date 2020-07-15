#!/usr/bin/env python
"""
Pymodbus Synchronous Server
--------------------------------------------------------------------------

The synchronous server is implemented in pure python without any third
party libraries (unless you need to use the serial protocols which require
pyserial). This is helpful in constrained or old environments where using
twisted is just not feasible. What follows is an example of its use:
"""
from pymodbus.server.sync import StartTcpServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def run_server(num_fields):
    # The slave context can also be initialized in zero_mode which means that a
    # request to address(0-7) will map to the address (0-7). The default is
    # False which is based on section 4.4 of the specification, so address(0-7)
    # will map to (1-8)::

    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0]*num_fields),
        co=ModbusSequentialDataBlock(0, [0]*num_fields),
        hr=ModbusSequentialDataBlock(0, [0]*num_fields),
        ir=ModbusSequentialDataBlock(0, [0]*num_fields))

    context = ModbusServerContext(slaves=store, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Modbus Slave'
    identity.ProductCode = 'MS'
    identity.ProductName = 'Streampipes Modbus Simulator'
    identity.ModelName = 'Modbus Slave'
    identity.MajorMinorRevision = '2.3.0'

    StartTcpServer(context, identity=identity, address=("localhost", 502))


if __name__ == "__main__":
    run_server(10)
