# producer.py
from kafka import KafkaProducer
import time
import json
import pandas as pd
import sys


class Reader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = pd.DataFrame()
        self.read_file()
        self.process_data()

    def read_file(self):
        self.data = pd.read_csv(self.file_name,
                                sep=',',
                                header='infer',
                                encoding='iso-8859-1')

    def process_data(self):
        columns_tmp = self.data.columns
        columns_tmp = [column_name.lower() for column_name in columns_tmp]
        self.data.columns = columns_tmp
        self.data.rename(columns={'open': 'open_price',
                                  'close': 'close_price',
                                  'adj close': 'adj_close'}, inplace=True)



class Producer:
    def __init__(self, file_name, topic, freq):
        self.topic = topic
        self.freq = freq if isinstance(freq, int) else int(freq)
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        self.reader = Reader(file_name)

    def start_write(self):
        for index, value in self.reader.data.iterrows():
            dict_data = dict(value)
            self.producer.send(self.topic, value=dict_data)
            print(f'Message {index + 1}: {dict_data}')
            time.sleep(self.freq)


if __name__ == '__main__':
    producer = Producer(sys.argv[1], sys.argv[2], sys.argv[3])
    producer.start_write()