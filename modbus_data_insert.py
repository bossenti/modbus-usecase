import pandas as pd
import time
from pymodbus.client.sync import ModbusTcpClient

if __name__ == "__main__":
    df_data = pd.read_csv("./data/flow.csv", sep=';')
    df_data.drop(['timestamp', 'sp_internal_label', 'sensorId', 'time'], axis=1, inplace=True)

    client = ModbusTcpClient('localhost')
    for idx, row in df_data.iterrows():
        for no, value in enumerate(row):
            client.write_register(no + 1, int(value))
        time.sleep(1)
