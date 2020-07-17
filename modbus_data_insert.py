import pandas as pd
import time
from pymodbus.client.sync import ModbusTcpClient

"""
    short script that writes the values of the flow data frame to Modbus registers
    Each value is updated after one second
"""

if __name__ == "__main__":

    # read in flow data from csv
    df_data = pd.read_csv("./data/flow.csv", sep=';')

    # drop data that are not of interest for this use case
    df_data.drop(['timestamp', 'sp_internal_label', 'sensorId', 'time'], axis=1, inplace=True)

    # start a Modbus Client on localhost
    client = ModbusTcpClient('localhost')

    # iterate over each row of the data frame
    for idx, row in df_data.iterrows():

        # write each value to the holding register, using another address for each column
        for no, value in enumerate(row):
            client.write_register(no + 1, int(value))

        # wait one second to overwrite values
        time.sleep(1)
